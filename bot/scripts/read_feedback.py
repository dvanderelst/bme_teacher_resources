#!/usr/bin/env python3
"""
Print the feedback teachers have filed, newest first.

    python bot/scripts/read_feedback.py

Reads the same database as everything else -- DATABASE_URL if it is set, the
local SQLite file if it is not -- and prints which one before anything else,
because an empty list means two very different things depending on the answer.

There is no filtering, no paging and no way to mark a report as handled. A
handful of teachers will not file enough for that to be the problem, and the
edition stamp on each report is what actually answers "is this still true?".
"""
import sys
import json
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # bot/

from lib.db import Database


def show_transcript(raw, scope):
    """Print what was attached, if anything.

    scope says what the transcript holds: "answer" is the single answer being
    reported, "conversation" is everything, which only happens when the teacher
    ticked the box.
    """
    if not raw:
        return
    try:
        messages = json.loads(raw)
    except ValueError:
        print("    (transcript could not be read)")
        return
    label = ("the whole conversation" if scope == "conversation"
             else "the answer reported")
    print(f"    -- {label}, {len(messages)} message(s) --")
    for message in messages:
        who = "teacher" if message.get("role") == "user" else "bot"
        body = textwrap.fill((message.get("content") or "").strip(),
                             width=72,
                             initial_indent="      ", subsequent_indent="      ")
        print(f"    {who}:")
        print(body)
        if message.get("sources"):
            print(f"      [from: {', '.join(message['sources'])}]")


def main():
    db = Database()
    db.create_schema()
    print(f"using {db.label}\n")

    rows = db.run(
        """
        SELECT submitted_at, username, sentiment, category, note, scope,
               transcript, conversation_id, edition, fingerprint
        FROM feedback ORDER BY submitted_at DESC
        """, fetch="all") or []
    if not rows:
        print("no feedback yet")
        return 0

    for (submitted, username, sentiment, category, note, scope, transcript,
         conversation_id, edition, fingerprint) in rows:
        mark = "＋" if sentiment == "up" else "－"
        when = str(submitted)[:19]
        print(f"{mark} {when}  {username}")
        if category:
            print(f"    {category}")
        if note:
            print(textwrap.fill(note, width=72,
                                initial_indent="    ", subsequent_indent="    "))
        # The stamp is the point of storing it: a complaint about the pairing
        # instructions means nothing without knowing which edition said what.
        print(f"    edition {edition} / {fingerprint}"
              + (f" / conversation {conversation_id}" if conversation_id else ""))
        show_transcript(transcript, scope)
        print()

    ups = sum(1 for row in rows if row[2] == "up")
    print(f"{len(rows)} report(s): {ups} positive, {len(rows) - ups} negative")
    return 0


if __name__ == "__main__":
    sys.exit(main())
