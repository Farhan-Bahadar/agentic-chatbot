from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


def get_response_from_ai_agent(
    llm_id,
    query,
    allow_search,
    system_prompt,
    provider
):

    # Select LLM
    if provider == "Groq":

        llm = ChatGroq(
            model=llm_id
        )

    elif provider == "OpenAI":

        llm = ChatOpenAI(
            model=llm_id
        )

    else:
        return "Invalid model provider."


    # Setup tools
    if allow_search:

        tools = [
            TavilySearch(
                max_results=2
            )
        ]

    else:
        tools = []


    # Default system prompt
    if not system_prompt.strip():

        system_prompt = (
            "Act as an AI chatbot who is smart, "
            "helpful, friendly, and accurate."
        )


    # Create agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )


    # Prepare message
    user_message = query[-1]

    state = {
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }


    # Invoke agent
    response = agent.invoke(state)


    # Get messages
    messages = response.get(
        "messages",
        []
    )


    # Extract AI messages
    ai_messages = [
        message.content
        for message in messages
        if isinstance(message, AIMessage)
    ]


    # Return final response
    if ai_messages:
        return ai_messages[-1]

    return "The AI agent did not return a response."