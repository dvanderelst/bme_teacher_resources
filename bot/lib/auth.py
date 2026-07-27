"""
Accounts for the teacher-support bot.

One account per teacher rather than a shared password. The reason is not the
login screen, which either way is a form: it is that a shared credential cannot
be revoked when it spreads, and that feedback collected under one has no author.
Code can be retrofitted later; the missing author on rows already collected
cannot.

Ported from the student agent, minus the columns that no longer apply.
"""
import time
from datetime import timedelta

import bcrypt

from lib.db import now

# Five failures in a five-minute rolling window locks the username until enough
# of them age out. By username only: behind a hosting proxy the client IP is the
# proxy's, so per-IP limiting would throttle everyone at once or nobody.
LOCKOUT_THRESHOLD = 5
LOCKOUT_WINDOW_MINUTES = 5

# Added to every failed login. Equalises the timing of the unknown-user and
# wrong-password paths, which otherwise differ by one bcrypt verification and
# so tell an attacker which usernames exist.
FAILED_LOGIN_DELAY_SECONDS = 0.5


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def create_user(db, username, password, full_name=None):
    db.run(
        "INSERT INTO users (username, password_hash, full_name, enabled, created_at) "
        "VALUES (?, ?, ?, 1, ?)",
        (username, hash_password(password), full_name, now()),
    )


def set_password(db, username, password):
    db.run("UPDATE users SET password_hash = ? WHERE username = ?",
           (hash_password(password), username))


def set_enabled(db, username, enabled):
    db.run("UPDATE users SET enabled = ? WHERE username = ?",
           (1 if enabled else 0, username))


def list_users(db):
    return db.run("SELECT username, full_name, enabled, created_at FROM users "
                  "ORDER BY username", fetch="all") or []


def is_locked_out(db, username):
    """Cheap count before bcrypt, so a script grinding one username cannot make
    us burn a hash per attempt."""
    cutoff = now() - timedelta(minutes=LOCKOUT_WINDOW_MINUTES)
    row = db.run("SELECT COUNT(*) FROM login_failures WHERE username = ? "
                 "AND attempted_at > ?", (username, cutoff), fetch="one")
    return bool(row) and row[0] >= LOCKOUT_THRESHOLD


def record_failure(db, username):
    db.run("INSERT INTO login_failures (username, attempted_at) VALUES (?, ?)",
           (username, now()))


def authenticate(db, username, password):
    """Return the user record on success, None otherwise.

    Always pays the delay on failure, and always runs a bcrypt comparison even
    for an unknown user, so the two failure modes take the same time.
    """
    row = db.run("SELECT username, password_hash, full_name, enabled FROM users "
                 "WHERE username = ?", (username,), fetch="one")
    stored = row[1] if row else "$2b$12$" + "x" * 53  # dummy, never matches
    ok = False
    try:
        ok = bcrypt.checkpw(password.encode(), stored.encode())
    except ValueError:
        ok = False
    if not row or not ok:
        record_failure(db, username)
        time.sleep(FAILED_LOGIN_DELAY_SECONDS)
        return None
    if not row[3]:
        time.sleep(FAILED_LOGIN_DELAY_SECONDS)
        return {"disabled": True}
    return {"username": row[0], "full_name": row[2], "disabled": False}
