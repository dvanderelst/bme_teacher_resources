"""
The chat page.

Every turn goes through moderation before it reaches the agent, and every answer
carries the documents it came from. Both are visible to the teacher on purpose:
for an audience being asked to trust this with a class, a filter they can see
working is worth more than one they are told about.

Feedback sits under each answer rather than in a general form, because the
report that is worth having is "this specific answer is wrong" and that is only
cheap to file while the answer is still on screen.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # bot/

import streamlit as st

from lib import agent, moderation
from lib.db import Database, save_feedback
from lib.settings import build_stamp, load_env

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
# Which answer has the report form open, and which have already been reported.
# Keyed by position in messages, which is stable for the life of a conversation
# and reset with it.
st.session_state.setdefault("feedback_open", None)
st.session_state.setdefault("feedback_sent", {})

user = st.session_state.user
name = user.get("full_name") or user["username"]

# One list, positive first. The sentiment column is derived from the choice
# rather than asked for separately: two controls that can disagree -- a thumbs
# up filed against "it is wrong" -- is a question nobody should have to answer.
POSITIVE = "It was helpful — nothing wrong with it"
CATEGORIES = [POSITIVE,
              "It is wrong or misleading",
              "It is not in the materials at all",
              "It is unclear or hard to follow",
              "It should not have been blocked",
              "Something else"]


@st.cache_resource
def get_db():
    db = Database()
    db.create_schema()
    return db


def open_report(index):
    st.session_state.feedback_open = index


def close_report():
    st.session_state.feedback_open = None


def file_report(index):
    """Store one report, and remember it so the button does not come back.

    Runs as a button callback rather than inline, which is what makes the form
    close cleanly: callbacks run before the page is redrawn, so the run that
    handles the click already knows the report is filed. Doing this inline and
    calling st.rerun() leaves the form on screen until the next click -- the
    rerun is requested from inside the form block and does not take.

    What travels with the report is a deliberate line. The assistant's answer
    always does: a report saying "this is wrong" that does not record what
    "this" was cannot be acted on weeks later, and the answer is the bot's own
    text, not the teacher's. The teacher's own questions travel only if they
    ask for it, which is the promise lib/db.py makes at the top of the file.

    A failure is kept and shown, not raised. Feedback is worth collecting, but
    not worth losing a teacher's place in a conversation over -- this runs
    while they are mid-lesson.
    """
    category = st.session_state.get(f"category_{index}") or CATEGORIES[0]
    note = st.session_state.get(f"note_{index}") or ""
    whole = st.session_state.get(f"whole_{index}", False)
    sentiment = "up" if category == POSITIVE else "down"

    if whole:
        scope, transcript = "conversation", st.session_state.messages
    else:
        scope, transcript = "answer", [st.session_state.messages[index]]
    edition, fingerprint = build_stamp()
    try:
        save_feedback(get_db(),
                      username=user["username"],
                      sentiment=sentiment,
                      category=category,
                      note=note.strip() or None,
                      scope=scope,
                      transcript=transcript,
                      conversation_id=st.session_state.conversation_id,
                      agent_id=config["AGENT_ID"],
                      edition=edition,
                      fingerprint=fingerprint)
    except Exception as exc:
        st.session_state.feedback_error = str(exc)
        return
    st.session_state.pop("feedback_error", None)
    st.session_state.feedback_sent[index] = sentiment
    st.session_state.feedback_open = None


def report_controls(index):
    """The feedback button under one answer, and the form it opens.

    One button rather than a thumbs pair. Thumbs are cheap to press and cheap
    to ignore, and what is actually worth having here is the sentence a teacher
    would write -- including when something worked, which a bare thumbs-up
    records without saying why. So every report goes through the same form, and
    the first category is the positive one.
    """
    if index in st.session_state.feedback_sent:
        st.caption("Thank you — that has been recorded.")
        return

    if st.session_state.feedback_open != index:
        st.button("Feedback", key=f"feedback_{index}",
                  help="Tell us about this answer — good or bad",
                  on_click=open_report, args=(index,))
        return

    with st.form(f"report_{index}"):
        st.selectbox("How was this answer?", CATEGORIES, key=f"category_{index}")
        st.text_area(
            "Anything you can tell us", key=f"note_{index}",
            placeholder="What the robot actually did, what the chapter says, "
                        "what you expected — or what worked well and why.")
        st.checkbox("Send this conversation with my report",
                    key=f"whole_{index}")
        st.caption("The answer above is included either way. Your own "
                   "questions are sent only if you tick the box.")
        send, cancel = st.columns([1, 1])
        send.form_submit_button("Send", type="primary",
                                on_click=file_report, args=(index,))
        cancel.form_submit_button("Cancel", on_click=close_report)


with st.sidebar:
    st.write(f"Signed in as **{name}**")
    if st.button("New conversation"):
        st.session_state.messages = []
        st.session_state.conversation_id = None
        st.session_state.feedback_open = None
        st.session_state.feedback_sent = {}
        st.rerun()
    if st.button("Log out"):
        st.session_state.clear()
        st.switch_page("app.py")

st.title("BmE teacher assistant")

# Said here, up front and at full size, rather than in a caption nobody reads.
# The claim is unusual enough to be worth the space -- most things teachers are
# asked to type into do keep what they type -- and it is only credible if it
# also says exactly when that stops being true.
st.info(
    "**Nothing you type here is stored.** Your questions and the answers are "
    "not logged, and no one at BmE can read this conversation.\n\n"
    "Answers come from the Biology Meets Engineering teacher materials. If "
    "something looks wrong, it probably is — and if something works well, that "
    "is worth knowing too. Use **Feedback** under any answer to tell us.\n\n"
    "That form is the only thing here that stores anything. It always includes "
    "the answer you are reporting on, because a report about an answer nobody "
    "can see is not much use. Your own questions are sent only if you tick the "
    "box that offers it.")

# Shown here rather than beside the thumbs, because a callback cannot draw to
# the page. Saying it plainly matters: a teacher who thinks they have reported
# something will not report it again.
if st.session_state.get("feedback_error"):
    st.error("That report could not be recorded, and has not been saved.")
    st.caption(f"({st.session_state.feedback_error})")

for index, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            st.caption("From: " + ", ".join(message["sources"]))
        elif message["role"] == "assistant":
            st.caption("No source document was used for this answer.")
        if message["role"] == "assistant":
            report_controls(index)

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
        # Rerun rather than stop, so the refusal comes back through the history
        # loop above and carries the thumbs like any other answer. "It should
        # not have been blocked" is a report worth having, and the refusal text
        # invites it.
        st.rerun()

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
    # The answer was just drawn by hand above, which is what shows during the
    # request. Rerunning redraws it through the history loop, where it picks up
    # its thumbs -- otherwise the newest answer, the one most likely to be
    # wrong, is the only one that cannot be reported until the next question.
    st.rerun()
