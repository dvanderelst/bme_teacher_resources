#!/usr/bin/env python3
"""
Talk to the deployed teacher-support bot from the terminal.

For checking what the agent actually says after a deploy, without going through
the web UI. It holds one conversation, so follow-up questions work the way a
teacher would ask them ("and which port for the colour sensor?").

The reason to test here rather than in a chat window is the source line printed
under every answer: the documents the agent retrieved to produce it. The one
failure that matters for this bot is a confident answer drawn from the model's
own knowledge of mBot rather than from these materials -- which reads exactly
like a good answer. An answer with no sources is flagged, because that is the
shape that failure takes.

    python bot/scripts/test_agent.py                    # interactive
    python bot/scripts/test_agent.py --ask "question"   # one-shot, for scripting

In the prompt: /new starts a fresh conversation, /raw dumps the last response,
/id prints the conversation id, /quit exits (as does Ctrl-D).

Environment, from bot/.env: MISTRAL_API_KEY, AGENT_ID
"""
import sys
import json
import argparse

from configure_agent import load_env, ENV_PATH  # same directory


def render(resp):
    """Pull the answer text, the cited documents and the tools used out of a
    response. Content arrives as a list of chunks -- prose interleaved with
    tool_reference markers -- so the text has to be reassembled in order."""
    text, sources, tools = [], [], []
    for out in resp.outputs:
        d = out.model_dump()
        if d.get("type") == "tool.execution":
            name = d.get("name")
            if name:
                tools.append(name)
            continue
        content = d.get("content")
        if isinstance(content, str):
            text.append(content)
        elif isinstance(content, list):
            for chunk in content:
                if not isinstance(chunk, dict):
                    continue
                if chunk.get("type") == "text":
                    text.append(chunk.get("text") or "")
                elif chunk.get("type") == "tool_reference":
                    title = chunk.get("title")
                    if title and title not in sources:
                        sources.append(title)
    return "".join(text).strip(), sources, tools


def show(resp):
    answer, sources, tools = render(resp)
    print(f"\n{answer}\n")
    if sources:
        print(f"  sources: {', '.join(sources)}")
    else:
        print("  sources: none -- this answer was not drawn from the materials")
    if tools:
        print(f"  tools:   {', '.join(sorted(set(tools)))}")
    usage = getattr(resp, "usage", None)
    if usage:
        d = usage.model_dump()
        total = d.get("total_tokens")
        if total:
            print(f"  tokens:  {total}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    ap.add_argument("--ask", help="ask one question, print the answer, exit")
    ap.add_argument("--agent-id", help="override AGENT_ID from bot/.env")
    args = ap.parse_args()

    config, missing = load_env(["MISTRAL_API_KEY", "AGENT_ID"])
    agent_id = args.agent_id or config.get("AGENT_ID")
    if not config.get("MISTRAL_API_KEY") or not agent_id:
        print(f"error: MISTRAL_API_KEY and AGENT_ID must be set in {ENV_PATH}")
        return 1

    from mistralai.client import Mistral
    client = Mistral(api_key=config["MISTRAL_API_KEY"])
    conversation = None

    def send(question):
        nonlocal conversation
        if conversation is None:
            resp = client.beta.conversations.start(agent_id=agent_id, inputs=question)
            conversation = resp.conversation_id
        else:
            resp = client.beta.conversations.append(
                conversation_id=conversation, inputs=question)
        return resp

    if args.ask:
        try:
            show(send(args.ask))
            return 0
        except Exception as e:
            print(f"error: {e}")
            return 1

    print(f"agent {agent_id}")
    print("ask a question, or /new /raw /id /quit\n")
    last = None
    while True:
        try:
            question = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not question:
            continue
        if question in ("/quit", "/exit"):
            return 0
        if question == "/new":
            conversation = None
            print("  started a new conversation\n")
            continue
        if question == "/id":
            print(f"  {conversation or 'no conversation yet'}\n")
            continue
        if question == "/raw":
            print(json.dumps(last.model_dump(), indent=2, default=str)
                  if last else "  nothing sent yet")
            continue
        try:
            last = send(question)
            show(last)
            print()
        except Exception as e:
            print(f"  error: {e}\n")


if __name__ == "__main__":
    sys.exit(main())
