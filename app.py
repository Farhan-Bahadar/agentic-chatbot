import streamlit as st

from ai_agent import get_response_from_ai_agent


# ==============================================
# PAGE CONFIGURATION
# ==============================================

st.set_page_config(
    page_title="Agentra - AI Chatbot Agent",
    page_icon="🤖",
    layout="centered"
)


# ==============================================
# HEADER
# ==============================================

st.title("🤖 Agentra")

st.write(
    "A configurable AI chatbot agent powered by "
    "Groq, OpenRouter, LangGraph, LangChain, and Tavily."
)


# ==============================================
# SYSTEM PROMPT
# ==============================================

system_prompt = st.text_area(
    "Define Your AI Agent:",
    height=100,
    placeholder=(
        "Example: You are a helpful AI assistant "
        "who explains technical topics to beginners."
    )
)


# ==============================================
# PROVIDER SELECTION
# ==============================================

provider = st.radio(
    "Select AI Provider:",
    [
        "Groq",
        "OpenRouter"
    ],
    horizontal=True
)


# ==============================================
# MODEL SELECTION
# ==============================================

if provider == "Groq":

    selected_model = st.selectbox(
        "Select Groq Model:",
        [
            "openai/gpt-oss-120b",
            "openai/gpt-oss-20b"
        ]
    )

else:

    selected_model = st.selectbox(
        "Select OpenRouter Model:",
        [
            "openrouter/free"
        ]
    )


# ==============================================
# WEB SEARCH
# ==============================================

allow_web_search = st.checkbox(
    "🌐 Allow Web Search",
    help="Use Tavily to search the web for current information."
)


# ==============================================
# USER QUERY
# ==============================================

user_query = st.text_area(
    "Enter Your Query:",
    height=150,
    placeholder="Ask anything..."
)


# ==============================================
# ASK AGENT
# ==============================================

if st.button(
    "Ask Agent!",
    type="primary"
):

    # ------------------------------------------
    # Validate Query
    # ------------------------------------------

    if not user_query.strip():

        st.warning(
            "Please enter a query."
        )


    # ------------------------------------------
    # Run Agent
    # ------------------------------------------

    else:

        try:

            with st.spinner(
                "Agentra is thinking..."
            ):

                response = get_response_from_ai_agent(
                    llm_id=selected_model,
                    query=[user_query],
                    allow_search=allow_web_search,
                    system_prompt=system_prompt,
                    provider=provider
                )


            # ------------------------------------------
            # Display Response
            # ------------------------------------------

            st.subheader("Agent Response")

            st.markdown(response)


        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )
