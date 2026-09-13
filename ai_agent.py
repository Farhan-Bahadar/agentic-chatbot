import os
import re
from typing import Any, Dict, List

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, ToolMessage
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

load_dotenv()

DEFAULT_SYSTEM_PROMPT = (
    "You are Agentra, a smart, helpful, accurate and friendly AI assistant. "
    "Answer the user's request clearly and directly. "
    "If web search is available and useful, use it before answering. "
    "Do not claim to have searched the web if you did not actually use the search tool."
)


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(
            f"Missing {name}. Add it to your .env file locally or your deployment secrets."
        )
    return value


def _build_llm(provider: str, llm_id: str):
    provider = provider.strip().lower()

    if provider == "groq":
        return ChatGroq(
            model=llm_id,
            groq_api_key=_require_env("GROQ_API_KEY"),
            temperature=0,
        )

    if provider == "openrouter":
        return ChatOpenAI(
            model=llm_id,
            openai_api_key=_require_env("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "https://agentra.streamlit.app",
                "X-Title": "Agentra - AI Agent Studio",
            },
            temperature=0,
        )

    raise ValueError(f"Unsupported provider: {provider}")


def _extract_sources(messages: List[Any]) -> List[str]:
    urls = []

    for message in messages:
        if not isinstance(message, ToolMessage):
            continue

        content = message.content
        if isinstance(content, list):
            content = " ".join(str(item) for item in content)
        else:
            content = str(content)

        for url in re.findall(r"https?://[^\s\]\)\"'<>]+", content):
            url = url.rstrip(".,;")
            if url not in urls:
                urls.append(url)

    return urls[:10]


def get_response_from_ai_agent(
    llm_id: str,
    query: str,
    allow_search: bool,
    system_prompt: str,
    provider: str,
) -> Dict[str, Any]:
    """Run Agentra's LangGraph ReAct agent."""

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    prompt = system_prompt.strip() or DEFAULT_SYSTEM_PROMPT
    llm = _build_llm(provider, llm_id)

    tools = []
    if allow_search:
        tools.append(
            TavilySearch(
                max_results=3,
                tavily_api_key=_require_env("TAVILY_API_KEY"),
            )
        )

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=prompt,
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query.strip(),
                }
            ]
        }
    )

    messages = result.get("messages", [])
    response = ""

    for message in reversed(messages):
        if isinstance(message, AIMessage) and message.content:
            content = message.content

            if isinstance(content, list):
                content = "\n".join(
                    item.get("text", str(item))
                    if isinstance(item, dict)
                    else str(item)
                    for item in content
                )

            response = str(content).strip()
            if response:
                break

    if not response:
        response = "The agent completed the task but did not return a readable response."

    return {
        "response": response,
        "sources": _extract_sources(messages) if allow_search else [],
    }
