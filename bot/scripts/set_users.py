#!/usr/bin/env python3
"""
Make the accounts in the database match bot/users.txt, exactly.

    python bot/scripts/set_users.py [path/to/users.txt]

Every account is deleted and rewritten from the file, so the file is the whole
account list rather than a log of commands that were run against it. That is
the point: with a handful of teachers, "who has access?" should be answerable
by reading one file, not by querying a database that remembers every add and
disable anyone ever typed.

Passwords are hashed on the way in; the database never holds the plaintext.
The file does, which is why it is gitignored -- see bot/users.txt.example.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # bot/

from lib import auth
from lib.db import Database
from lib.settings import BOT_DIR

MIN_PASSWORD_LENGTH = 12


def parse(path):
    """Read the file into [(username, password, full_name)].

    Returns (users, errors). Nothing is applied unless errors is empty: a
    half-written account list is worse than none, because the accounts that
    did land make it look like the run succeeded.
    """
    users, errors, seen = [], [], set()
    for number, raw in enumerate(path.read_text().splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        # maxsplit=2, so the full name keeps its spaces and nothing else can.
        fields = line.split(maxsplit=2)
        if len(fields) < 2:
            errors.append(f"line {number}: needs a username and a password")
            continue
        username, password = fields[0], fields[1]
        full_name = fields[2].strip() if len(fields) > 2 else None
        if len(password) < MIN_PASSWORD_LENGTH:
            errors.append(f"line {number}: {username}'s password is under "
                          f"{MIN_PASSWORD_LENGTH} characters")
        if username in seen:
            errors.append(f"line {number}: {username} appears twice")
        seen.add(username)
        users.append((username, password, full_name))
    if not users and not errors:
        errors.append("no accounts in the file -- that would delete everyone")
    return users, errors


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else BOT_DIR / "users.txt"
    if not path.exists():
        print(f"error: {path} does not exist")
        print("copy bot/users.txt.example to bot/users.txt and edit it")
        return 1

    users, errors = parse(path)
    if errors:
        print(f"{path}:")
        for error in errors:
            print(f"  {error}")
        print("\nnothing was changed")
        return 1

    db = Database()
    db.create_schema()
    # Printed before anything else on purpose. Pointing the script at the wrong
    # database is the mistake that costs time here -- accounts written to a
    # local file while the app reads Postgres look exactly like a wrong
    # password at the login screen.
    print(f"using {db.label}")
    print(f"reading {path}\n")

    existing = {row[0] for row in auth.list_users(db)}
    wanted = {username for username, _, _ in users}
    for username in sorted(wanted):
        print(f"  {'set':7} {username}" if username in existing
              else f"  {'new':7} {username}")
    for username in sorted(existing - wanted):
        print(f"  {'DELETE':7} {username}")

    try:
        if input("\nproceed? [y/N] ").strip().lower() not in ("y", "yes"):
            print("nothing was changed")
            return 1
    except (EOFError, KeyboardInterrupt):
        print("\nnothing was changed")
        return 1

    # Hash before deleting. bcrypt is slow by design and this is where a typo
    # in the file would surface; doing it first means a failure here leaves the
    # existing accounts alone.
    rows = [(username, auth.hash_password(password), full_name)
            for username, password, full_name in users]
    db.run("DELETE FROM users")
    for username, password_hash, full_name in rows:
        auth.insert_user(db, username, password_hash, full_name)
    print(f"\n{len(rows)} account(s) set")
    return 0


if __name__ == "__main__":
    sys.exit(main())
