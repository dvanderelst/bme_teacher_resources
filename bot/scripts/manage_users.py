#!/usr/bin/env python3
"""
Add, disable and re-password teacher accounts.

There is no self-service signup and no password reset by email. The cohort is
small enough to be managed by hand, and every route that does not exist is one
that cannot be abused.

    python bot/scripts/manage_users.py list
    python bot/scripts/manage_users.py add dieter --name "Dieter Vanderelst"
    python bot/scripts/manage_users.py password dieter
    python bot/scripts/manage_users.py disable dieter
    python bot/scripts/manage_users.py enable dieter

Passwords are prompted for, never passed on the command line, so they do not
land in shell history.
"""
import sys
import getpass
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # bot/

from lib import auth
from lib.db import Database


def ask_password():
    first = getpass.getpass("Password: ")
    if len(first) < 12:
        print("error: use at least 12 characters")
        return None
    if first != getpass.getpass("Again: "):
        print("error: they do not match")
        return None
    return first


def main():
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    add = sub.add_parser("add")
    add.add_argument("username")
    add.add_argument("--name", default=None)
    for name in ("password", "disable", "enable"):
        p = sub.add_parser(name)
        p.add_argument("username")
    args = ap.parse_args()

    db = Database()
    db.create_schema()
    print(f"using {db.label}\n")

    if args.command == "list":
        rows = auth.list_users(db)
        if not rows:
            print("no accounts yet")
            return 0
        for username, full_name, enabled, created in rows:
            state = "enabled" if enabled else "DISABLED"
            print(f"  {username:20} {state:9} {full_name or ''}")
        return 0

    if args.command == "add":
        password = ask_password()
        if not password:
            return 1
        try:
            auth.create_user(db, args.username, password, args.name)
        except Exception as e:
            print(f"error: could not add {args.username}: {e}")
            return 1
        print(f"added {args.username}")
        return 0

    if args.command == "password":
        password = ask_password()
        if not password:
            return 1
        auth.set_password(db, args.username, password)
        print(f"password changed for {args.username}")
        return 0

    auth.set_enabled(db, args.username, args.command == "enable")
    print(f"{args.username} {args.command}d")
    return 0


if __name__ == "__main__":
    sys.exit(main())
