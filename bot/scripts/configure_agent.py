#!/usr/bin/env python3
"""
Push the generated knowledge set to Mistral and configure the agent that reads it.

    bot/knowledge/*.md  ->  Mistral library  ->  agent (document_library tool)

Run this after book/build.sh, which regenerates bot/knowledge/. The two together
are the release: the chapters, the PDF and what the bot knows all move at once.

The library is treated as a *mirror*, not an inbox. Documents are deleted and
re-uploaded rather than added, because uploading is not idempotent and the
failure mode is bad in a specific way: run this twice and the library holds two
copies of every chapter, run it after an edition change and it holds two
editions. The bot then answers from both at once, which is the one failure this
whole design exists to prevent -- a teacher being told something the PDF in
their hand contradicts.

The edition and git fingerprint from bot/knowledge/manifest.json are written
into the agent's metadata and version message, so a deployed agent can always be
traced back to the edition it was built from.

Instructions are sent as the agent's system prompt and are NOT uploaded to the
library. They describe how to behave, not what is true; in the library they
would be retrievable as though they were course material, and the bot could
quote its own rulebook back to a teacher.

    python bot/scripts/configure_agent.py --dry-run   # show the plan, change nothing
    python bot/scripts/configure_agent.py             # apply it

Environment, from bot/.env (gitignored -- it holds a key):
    MISTRAL_API_KEY, MISTRAL_LIBRARY_ID, AGENT_ID
"""
import os
import re
import sys
import json
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BOT_DIR = SCRIPT_DIR.parent
KNOWLEDGE_DIR = BOT_DIR / "knowledge"
INSTRUCTIONS = BOT_DIR / "instructions.md"
ENV_PATH = BOT_DIR / ".env"

AGENT_NAME = "BmE Teacher Support Bot"
AGENT_DESCRIPTION = "Assistant for teachers using the Biology Meets Engineering materials"
DEFAULT_MODEL = "mistral-large-latest"
DEFAULT_TEMPERATURE = 0.2


def load_env(required):
    """Read bot/.env. Returns {} rather than exiting when the file is absent, so
    --dry-run still works on a machine that has never been given a key."""
    config = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip().strip('"').strip("'")
    missing = [k for k in required if not config.get(k)]
    return config, missing


def read_manifest():
    """Edition and fingerprint, so the deployed agent can be traced to a build."""
    path = KNOWLEDGE_DIR / "manifest.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def local_documents():
    return sorted(KNOWLEDGE_DIR.glob("*.md"))


def remote_documents(client, library_id):
    """Every document in the library, following pagination."""
    out, page = [], 0
    while True:
        resp = client.beta.libraries.documents.list(
            library_id=library_id, page=page, page_size=100)
        batch = list(getattr(resp, "data", None) or [])
        out += batch
        if len(batch) < 100:
            return out
        page += 1


def sync_documents(client, library_id, dry_run):
    """Mirror bot/knowledge/*.md into the library. Returns a list of failures."""
    local = local_documents()
    if not local:
        return [f"no documents in {KNOWLEDGE_DIR} -- run book/build.sh first"]

    existing = []
    if client:
        # Listing has to succeed before anything is uploaded. If it does not, we
        # cannot know what is already there, and uploading regardless is how the
        # library ends up holding two editions at once.
        try:
            existing = remote_documents(client, library_id)
        except Exception as e:
            if not dry_run:
                return [f"cannot list library {library_id}: {e}",
                        "refusing to upload without knowing what is already there"]
            print(f"  cannot read the library ({e})")
            print("  showing the local plan only")

    ours = {p.name for p in local}
    # Everything markdown is ours to manage, including names we no longer emit:
    # a renamed chapter (15-block-reference.md -> 57-) would otherwise linger
    # forever as a second, stale answer to the same question.
    stale = [d for d in existing if (d.name or "").endswith(".md")]
    foreign = [d for d in existing if not (d.name or "").endswith(".md")]

    print(f"  local {len(local)} documents, library holds {len(existing)}")
    for d in foreign:
        print(f"  leaving alone (not markdown): {d.name}")

    failures = []
    for d in stale:
        mark = "would delete" if dry_run else "deleting"
        note = "" if d.name in ours else "  [no longer produced]"
        print(f"  {mark} {d.name}{note}")
        if dry_run:
            continue
        try:
            client.beta.libraries.documents.delete(
                library_id=library_id, document_id=d.id)
        except Exception as e:
            failures.append(f"delete {d.name}: {e}")

    for path in local:
        print(f"  {'would upload' if dry_run else 'uploading'} {path.name}")
        if dry_run:
            continue
        try:
            client.beta.libraries.documents.upload(
                library_id=library_id,
                file={"file_name": path.name,
                      "content": path.read_bytes()})
        except Exception as e:
            failures.append(f"upload {path.name}: {e}")
    return failures


def configure_library(client, library_id, manifest, dry_run):
    name = "BmE Teacher Resources"
    desc = (f"Knowledge set for the BmE teacher-support bot. "
            f"Edition {manifest.get('edition', 'unknown')}, "
            f"fingerprint {manifest.get('fingerprint', 'unknown')}. "
            f"Generated by book/tools/knowledge.py -- do not edit here.")
    print(f"  {'would set' if dry_run else 'setting'} library name and description")
    if dry_run:
        return []
    try:
        client.beta.libraries.update(
            library_id=library_id, name=name, description=desc)
        return []
    except Exception as e:
        return [f"library update: {e}"]


def configure_agent(client, agent_id, library_id, manifest, model,
                    temperature, reasoning_effort, dry_run):
    if not INSTRUCTIONS.exists():
        return [f"{INSTRUCTIONS} not found"]
    # Sent verbatim. Stripping the headings and blank lines out of a structured
    # prompt only destroys the structure the model is meant to follow.
    instructions = INSTRUCTIONS.read_text(encoding="utf-8")

    edition = manifest.get("edition", "unknown")
    fingerprint = manifest.get("fingerprint", "unknown")

    print(f"  model {model}, temperature {temperature}"
          + (f", reasoning_effort {reasoning_effort}" if reasoning_effort else "")
          + f"\n  library tool -> {library_id}"
          + f"\n  instructions {len(instructions.split())} words from {INSTRUCTIONS.name}"
          + f"\n  stamped {edition} / {fingerprint}")
    if dry_run:
        return []

    from mistralai.client.models.completionargs import CompletionArgs
    from mistralai.client.models.documentlibrarytool import DocumentLibraryTool

    args = {"temperature": temperature}
    if reasoning_effort:
        args["reasoning_effort"] = reasoning_effort

    try:
        client.beta.agents.update(
            agent_id=agent_id,
            name=AGENT_NAME,
            description=AGENT_DESCRIPTION,
            model=model,
            instructions=instructions,
            tools=[DocumentLibraryTool(library_ids=[library_id])],
            completion_args=CompletionArgs(**args),
            metadata={"edition": edition,
                      "fingerprint": fingerprint,
                      "documents": str(len(local_documents())),
                      "generated_by": "book/tools/knowledge.py"},
            version_message=f"BmE {edition} ({fingerprint})",
        )
        return []
    except Exception as e:
        return [f"agent update: {e}"]


def main():
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    ap.add_argument("--dry-run", action="store_true",
                    help="show the plan and change nothing")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    ap.add_argument("--reasoning-effort", default=None,
                    choices=["none", "minimal", "low", "medium", "high", "xhigh"],
                    help="omitted entirely unless given")
    args = ap.parse_args()

    required = ["MISTRAL_API_KEY", "MISTRAL_LIBRARY_ID", "AGENT_ID"]
    config, missing = load_env(required)
    if missing and not args.dry_run:
        print(f"error: {', '.join(missing)} missing from {ENV_PATH}")
        return 1

    manifest = read_manifest()
    if not manifest:
        print(f"warning: no manifest in {KNOWLEDGE_DIR} -- "
              f"the agent will be stamped 'unknown'")
    if re.search(r"-(stale|dirty)", str(manifest.get("fingerprint", ""))):
        print(f"warning: fingerprint {manifest['fingerprint']} was built from a "
              f"dirty tree; commit before deploying")

    client = None
    if not missing:
        from mistralai.client import Mistral
        client = Mistral(api_key=config["MISTRAL_API_KEY"])
    elif args.dry_run:
        print(f"note: {', '.join(missing)} unset -- showing the local plan only")

    print(f"\n=== BmE teacher bot {'(dry run)' if args.dry_run else ''} ===")
    print(f"edition {manifest.get('edition', 'unknown')}  "
          f"fingerprint {manifest.get('fingerprint', 'unknown')}\n")

    failures = []
    print("documents:")
    failures += sync_documents(client, config.get("MISTRAL_LIBRARY_ID"), args.dry_run or not client)
    print("\nlibrary:")
    if client:
        failures += configure_library(client, config["MISTRAL_LIBRARY_ID"],
                                      manifest, args.dry_run)
    print("\nagent:")
    failures += configure_agent(client, config.get("AGENT_ID"),
                                config.get("MISTRAL_LIBRARY_ID"), manifest,
                                args.model, args.temperature,
                                args.reasoning_effort,
                                args.dry_run or not client)

    if failures:
        print(f"\n{len(failures)} step(s) failed:")
        for f in failures:
            print(f"  {f}")
        return 1
    print("\ndone." if not args.dry_run else "\ndry run only -- nothing changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
