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
import os
from pathlib import Path

BOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BOT_DIR / ".env"
KNOWLEDGE_DIR = BOT_DIR / "knowledge"
INSTRUCTIONS = BOT_DIR / "instructions.md"


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
    for key in set(required) | set(config):
        if os.environ.get(key):
            config[key] = os.environ[key]
    return config, [k for k in required if not config.get(k)]


def get(key, default=None):
    config, _ = load_env()
    return config.get(key, default)
