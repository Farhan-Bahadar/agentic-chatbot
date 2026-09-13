from dotenv import load_dotenv
import os

load_dotenv()

# --------------------------------
# Imports
# --------------------------------

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


# --------------------------------
# Main AI Agent Function
# --------------------------------

def get_response_from_ai_agent(
    llm_id,
    query,
    allow_search,
    system_prompt,
    provider
):

    # ==============================================
    # GROQ
    # ==============================================

    if provider == "Groq":

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            return "GROQ_API_KEY is missing from your .env file."

        llm = ChatGroq(
            model=llm_id,
            temperature=0,
            api_key=api_key
        )


    # ==============================================
    # OPENROUTER
    # ==============================================

    elif provider == "OpenRouter":

        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            return "OPENROUTER_API_KEY is missing from your .env file."

        llm = ChatOpenAI(
            model=llm_id,
            temperature=0,
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "https://agentra.streamlit.app",
                "X-Title": "Agentra - AI Chatbot Agent"
            }
        )


    # ==============================================
    # INVALID PROVIDER
    # ==============================================

    else:

        return "Invalid AI provider selected."


    # ==============================================
    # TAVILY WEB SEARCH
    # ==============================================

    tools = []

    if allow_search:

        tavily_api_key = os.getenv("TAVILY_API_KEY")

        if not tavily_api_key:
            return "TAVILY_API_KEY is missing from your .env file."

        tools = [
            TavilySearch(
                max_results=3,
                tavily_api_key=tavily_api_key
            )
        ]


    # ==============================================
    # DEFAULT SYSTEM PROMPT
    # ==============================================

    if not system_prompt.strip():

        system_prompt = (
            "You are Agentra, a smart, helpful, friendly, "
            "and accurate AI assistant. "
            "Give clear and useful answers."
        )


    # ==============================================
    # CREATE LANGGRAPH AGENT
    # ==============================================

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )


    # ==============================================
    # USER MESSAGE
    # ==============================================

    user_message = query[-1]

    state = {
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }


    # ==============================================
    # RUN AGENT
    # ==============================================

    response = agent.invoke(state)


    # ==============================================
    # GET MESSAGES
    # ==============================================

    messages = response.get(
        "messages",
        []
    )


    # ==============================================
    # EXTRACT FINAL AI RESPONSE
    # ==============================================

    ai_messages = [
        message.content
        for message in messages
        if isinstance(message, AIMessage)
    ]


    if ai_messages:

        return ai_messages[-1]


    return "The AI agent did not return a response."

