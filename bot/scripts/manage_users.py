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


def ask(prompt):
    """Prompt, or give up quietly on Ctrl-C / Ctrl-D rather than tracebacking."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return ""


def resolve_username(db, given, must_exist):
    """Take the username from the command line or ask for it, then check it.

    The check runs whichever way the name arrived. Doing it only on the
    prompted path left `disable someone-who-does-not-exist` updating no rows
    and reporting success, which is worse than an error: it tells you an
    account is disabled when nothing of the sort happened.

    Checking here rather than letting the database raise also turns "duplicate
    key value violates unique constraint" into a sentence.
    """
    name = given if given is not None else ask("Username: ")
    if not name:
        print("error: no username given")
        return None
    if " " in name:
        print("error: usernames cannot contain spaces")
        return None
    known = {row[0] for row in auth.list_users(db)}
    if must_exist and name not in known:
        print(f"error: there is no account called {name}")
        return None
    if not must_exist and name in known:
        print(f"error: {name} already exists — use `password {name}` to change it")
        return None
    return name


def ask_password():
    try:
        first = getpass.getpass("Password: ")
        if len(first) < 12:
            print("error: use at least 12 characters")
            return None
        if first != getpass.getpass("Again: "):
            print("error: they do not match")
            return None
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    return first


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    # Not required=True: a bare run should show the usage examples in the module
    # docstring above, which is what someone reaching for this actually needs,
    # rather than one line naming the argument they omitted.
    sub = ap.add_subparsers(dest="command")
    sub.add_parser("list")
    # username is optional throughout: given, it is used; omitted, it is asked
    # for. The argument form is what makes the commands scriptable, the prompt
    # is what makes them usable once, by hand, six months from now.
    add = sub.add_parser("add")
    add.add_argument("username", nargs="?", default=None)
    add.add_argument("--name", default=None, help="full name, for display")
    for name in ("password", "disable", "enable"):
        p = sub.add_parser(name)
        p.add_argument("username", nargs="?", default=None)
    args = ap.parse_args()
    if not args.command:
        ap.print_help()
        return 1

    db = Database()
    db.create_schema()
    # Printed before anything else on purpose. Pointing the script at the wrong
    # database is the mistake that costs time here -- an account created in a
    # local file while the app reads Postgres looks exactly like a wrong
    # password at the login screen.
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
        username = resolve_username(db, args.username, must_exist=False)
        if not username:
            return 1
        full_name = args.name if args.name is not None else ask("Full name (optional): ")
        password = ask_password()
        if not password:
            return 1
        try:
            auth.create_user(db, username, password, full_name or None)
        except Exception as e:
            print(f"error: could not add {username}: {e}")
            return 1
        print(f"added {username}")
        return 0

    username = resolve_username(db, args.username, must_exist=True)
    if not username:
        return 1

    if args.command == "password":
        password = ask_password()
        if not password:
            return 1
        auth.set_password(db, username, password)
        print(f"password changed for {username}")
        return 0

    auth.set_enabled(db, username, args.command == "enable")
    print(f"{username} {args.command}d")
    return 0


if __name__ == "__main__":
    sys.exit(main())
