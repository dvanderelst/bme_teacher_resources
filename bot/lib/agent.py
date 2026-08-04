"""
Talking to the deployed Mistral agent.

Conversation state lives on Mistral's side -- `append` needs it, that is how a
follow-up question knows what came before. Worth being precise about when
telling teachers what happens to their chats: we keep no copy, which is not the
same as no copy existing.

Answers arrive as a list of chunks, prose interleaved with tool_reference
markers naming the documents used. The references are pulled out rather than
dropped because they are the only evidence that an answer came from the
materials at all, and an answer with none is the failure mode this bot has.
"""
from dataclasses import dataclass, field


@dataclass
class Answer:
    text: str
    sources: list = field(default_factory=list)
    conversation_id: str = None
    grounded: bool = True


def _render(response):
    text, sources = [], []
    for output in response.outputs:
        d = output.model_dump()
        if d.get("type") == "tool.execution":
            continue
        content = d.get("content")
        if isinstance(content, str):
            text.append(content)
        elif isinstance(content, list):
            for chunk in content:
                if not isinstance(chunk, dict):
                    continue
                if chunk.get("type") == "text":
                    text.append(chunk.get("text") or "")
                elif chunk.get("type") == "tool_reference":
                    title = chunk.get("title")
                    if title and title not in sources:
                        sources.append(title)
    return "".join(text).strip(), sources


def ask(client, agent_id, question, conversation_id=None):
    if conversation_id:
        response = client.beta.conversations.append(
            conversation_id=conversation_id, inputs=question)
    else:
        response = client.beta.conversations.start(
            agent_id=agent_id, inputs=question)
    text, sources = _render(response)
    return Answer(text=text, sources=sources,
                  conversation_id=response.conversation_id,
                  grounded=bool(sources))
