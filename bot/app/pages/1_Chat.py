"""
The chat page.

Every turn goes through moderation before it reaches the agent, and every answer
carries the documents it came from. Both are visible to the teacher on purpose:
for an audience being asked to trust this with a class, a filter they can see
working is worth more than one they are told about.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # bot/

import streamlit as st

from lib import agent, moderation
from lib.settings import load_env

st.set_page_config(page_title="BmE Teacher Chat", page_icon="🤖", layout="centered")
st.markdown("<style>[data-testid='stSidebarNav'] {display: none;}</style>",
            unsafe_allow_html=True)

if not st.session_state.get("user"):
    st.switch_page("app.py")

config, missing = load_env(["MISTRAL_API_KEY", "AGENT_ID"])
if missing:
    st.error("The assistant is not configured. Please contact the BmE team.")
    st.caption(f"missing: {', '.join(missing)}")
    st.stop()


@st.cache_resource
def get_client():
    from mistralai.client import Mistral
    return Mistral(api_key=config["MISTRAL_API_KEY"])


client = get_client()
st.session_state.setdefault("messages", [])
st.session_state.setdefault("conversation_id", None)

user = st.session_state.user
name = user.get("full_name") or user["username"]

with st.sidebar:
    st.write(f"Signed in as **{name}**")
    if st.button("New conversation"):
        st.session_state.messages = []
        st.session_state.conversation_id = None
        st.rerun()
    if st.button("Log out"):
        st.session_state.clear()
        st.switch_page("app.py")

st.title("BmE teacher assistant")
st.caption("Answers come from the Biology Meets Engineering teacher materials. "
           "If something looks wrong, it probably is — please say so.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            st.caption("From: " + ", ".join(message["sources"]))
        elif message["role"] == "assistant":
            st.caption("No source document was used for this answer.")

question = st.chat_input("Ask about the materials, the robot or mBlock")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    verdict = moderation.check(client, question)
    if not verdict.allowed:
        # Say which category stopped it. A refusal with no reason is what makes
        # people distrust a system, and here the transparency is the point.
        refusal = (f"I can't send that one on — it was flagged as "
                   f"**{verdict.reason}**. Please rephrase, and if you think "
                   f"that is wrong, mention it in the feedback.")
        with st.chat_message("assistant"):
            st.warning(refusal)
        st.session_state.messages.append(
            {"role": "assistant", "content": refusal, "sources": []})
        st.stop()

    if verdict.warnings:
        st.info(f"Heads up: this looks like it may contain {verdict.reason}. "
                f"It has been sent, but avoid identifying details about students.")

    with st.chat_message("assistant"):
        with st.spinner("Looking it up…"):
            try:
                answer = agent.ask(client, config["AGENT_ID"], question,
                                   st.session_state.conversation_id)
            except Exception as exc:
                st.error("Something went wrong reaching the assistant.")
                st.caption(f"({exc})")
                st.stop()
        st.session_state.conversation_id = answer.conversation_id
        st.markdown(answer.text)
        if answer.sources:
            st.caption("From: " + ", ".join(answer.sources))
        else:
            st.caption("No source document was used for this answer.")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer.text, "sources": answer.sources})
