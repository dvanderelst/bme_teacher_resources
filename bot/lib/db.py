"""
Storage for accounts and feedback.

Postgres in production, SQLite locally. The two are worth supporting because
the alternative is that nobody can run the app without provisioning a database
first, and an app that cannot be run locally does not get tested. SQLite is not
an option in production: hosting containers have ephemeral filesystems, so the
file would vanish on every redeploy, taking the accounts with it.

The SQL is kept to the intersection of both dialects -- TEXT, INTEGER,
TIMESTAMP, no JSONB, no SERIAL -- so the schema statements are shared rather
than written twice. JSON payloads are stored as TEXT and encoded by the caller.

Only two tables. Interactions are deliberately not logged: nothing a teacher
types is stored unless they choose to send it with a piece of feedback.
"""
import json
import sqlite3
from datetime import datetime, timezone

from lib.settings import BOT_DIR, load_env

SCHEMA = [
    """
    CREATE TABLE IF NOT EXISTS users (
        username      TEXT PRIMARY KEY,
        password_hash TEXT NOT NULL,
        full_name     TEXT,
        enabled       INTEGER NOT NULL DEFAULT 1,
        created_at    TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS login_failures (
        username     TEXT NOT NULL,
        attempted_at TIMESTAMP
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_login_failures ON login_failures (username, attempted_at)",
    """
    CREATE TABLE IF NOT EXISTS feedback (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        submitted_at    TIMESTAMP,
        username        TEXT,
        sentiment       TEXT,
        category        TEXT,
        note            TEXT,
        scope           TEXT,
        transcript      TEXT,
        conversation_id TEXT,
        agent_id        TEXT,
        edition         TEXT,
        fingerprint     TEXT
    )
    """,
]

# Postgres has no AUTOINCREMENT and wants a different serial spelling.
PG_FIXUPS = [("INTEGER PRIMARY KEY AUTOINCREMENT", "SERIAL PRIMARY KEY")]


class Database:
    """A connection plus the dialect differences that leak past the SQL above."""

    def __init__(self, url=None):
        if url is None:
            url = load_env()[0].get("DATABASE_URL", "")
        self.url = url
        self.postgres = url.startswith("postgres")
        if self.postgres:
            import psycopg2
            self._connect = lambda: psycopg2.connect(url, connect_timeout=10)
            self.placeholder = "%s"
        else:
            path = BOT_DIR / "local.db"
            self._connect = lambda: sqlite3.connect(path)
            self.placeholder = "?"
        self.label = "postgres" if self.postgres else f"sqlite ({BOT_DIR / 'local.db'})"

    def _sql(self, statement):
        if not self.postgres:
            return statement
        for old, new in PG_FIXUPS:
            statement = statement.replace(old, new)
        return statement

    def run(self, statement, params=(), fetch=None):
        """fetch: None, "one" or "all"."""
        # Statements are written with "?" and translated, rather than each
        # caller knowing which driver is behind it.
        statement = self._sql(statement).replace("?", self.placeholder)
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(statement, params)
            result = None
            if fetch == "one":
                result = cur.fetchone()
            elif fetch == "all":
                result = cur.fetchall()
            conn.commit()
            return result
        finally:
            conn.close()

    def create_schema(self):
        for statement in SCHEMA:
            self.run(statement)


def now():
    return datetime.now(timezone.utc)


def save_feedback(db, *, username, sentiment, category, note, scope, transcript,
                  conversation_id, agent_id, edition, fingerprint):
    """Store one piece of feedback.

    edition and fingerprint are not decoration. Without them a report that the
    pairing instructions are wrong cannot be told apart from one filed before
    the pairing instructions were fixed, and the whole point of collecting these
    is to act on them weeks later.
    """
    db.run(
        """
        INSERT INTO feedback (submitted_at, username, sentiment, category, note,
                              scope, transcript, conversation_id, agent_id,
                              edition, fingerprint)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (now(), username, sentiment, category, note, scope,
         json.dumps(transcript, ensure_ascii=False) if transcript else None,
         conversation_id, agent_id, edition, fingerprint),
    )
