"""
Configuration for the scripts and the app, from one place.

Precedence is environment first, then bot/.env. That order is the point: a
hosting platform supplies secrets as environment variables and there is no .env
file on the box, so a loader that reads only the file works locally and nowhere
else. Reading the environment first also makes a one-off override on the command
line do what it looks like it does.

There is deliberately no secrets.toml. Streamlit's st.secrets is file-based, so
using it would mean generating that file from environment variables at deploy --
machinery whose only purpose is to satisfy a file format, and a second place for
the same key to live and disagree.
"""
import json
import os
from pathlib import Path

BOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BOT_DIR / ".env"
KNOWLEDGE_DIR = BOT_DIR / "knowledge"
INSTRUCTIONS = BOT_DIR / "instructions.md"

# Every name that may arrive from the real environment instead of bot/.env.
#
# It has to be written down somewhere, because the overlay below can only look
# up keys it already knows the name of, and on a hosting platform there is no
# .env file to learn them from. A key missing from this list is therefore
# invisible in production however carefully it is set on the service.
#
# That failure is silent, which is what makes it worth a list. DATABASE_URL was
# missing here, so the deployed app read no URL, fell back to a container-local
# SQLite file, and rejected every login against an empty table -- while the
# Postgres it was pointed at sat there correctly populated. Nothing in the logs
# said so: SQLite creates its file on demand, so there was no error to see.
KNOWN_KEYS = ("MISTRAL_API_KEY", "AGENT_ID", "MISTRAL_LIBRARY_ID", "DATABASE_URL")


def load_env(required=()):
    """Return (config, missing). Never raises and never exits: callers decide
    whether a missing key is fatal, because --dry-run paths need to run without
    one."""
    config = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip().strip('"').strip("'")
    for key in set(required) | set(config) | set(KNOWN_KEYS):
        if os.environ.get(key):
            config[key] = os.environ[key]
    return config, [k for k in required if not config.get(k)]


def get(key, default=None):
    config, _ = load_env()
    return config.get(key, default)


def build_stamp():
    """Return (edition, fingerprint) from the knowledge manifest.

    Stamped onto every piece of feedback. Without it a report that the pairing
    instructions are wrong cannot be told apart from one filed before they were
    fixed, and these are meant to be acted on weeks later.

    It has to come from the manifest rather than from git: the running
    container has no history to ask. bot/knowledge/ is committed, which is what
    makes this readable in production at all.
    """
    try:
        manifest = json.loads((KNOWLEDGE_DIR / "manifest.json").read_text())
    except (OSError, ValueError):
        return "unknown", "unknown"
    return (manifest.get("edition", "unknown"),
            manifest.get("fingerprint", "unknown"))
