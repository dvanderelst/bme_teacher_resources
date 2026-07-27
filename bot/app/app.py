"""
Login. The only page reachable without an account.

Streamlit's multipage routing exposes every file under pages/ by URL, so the
sidebar is hidden and the chat page checks the session itself. Hiding the
sidebar is presentation; the check on the other side is the control.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # bot/

import streamlit as st

from lib.auth import authenticate, is_locked_out, LOCKOUT_WINDOW_MINUTES
from lib.db import Database

st.set_page_config(page_title="BmE Teacher Chat", page_icon="🤖")
st.markdown("<style>[data-testid='stSidebarNav'] {display: none;}</style>",
            unsafe_allow_html=True)

if st.session_state.get("user"):
    st.switch_page("pages/1_Chat.py")


@st.cache_resource
def get_db():
    db = Database()
    db.create_schema()
    return db


try:
    db = get_db()
except Exception as exc:
    st.error("The assistant is temporarily unavailable. Please try again later.")
    st.caption(f"({exc})")
    st.stop()

st.title("Biology Meets Engineering")
st.write("Teacher assistant. Please log in.")

with st.form("login"):
    username = st.text_input("Username").strip()
    password = st.text_input("Password", type="password")
    if st.form_submit_button("Log in"):
        if is_locked_out(db, username):
            st.error(f"Too many failed attempts. Please wait about "
                     f"{LOCKOUT_WINDOW_MINUTES} minutes and try again.")
        else:
            user = authenticate(db, username, password)
            if user is None:
                st.error("Incorrect username or password.")
            elif user.get("disabled"):
                st.error("This account is not currently active.")
            else:
                st.session_state.user = user
                st.switch_page("pages/1_Chat.py")
