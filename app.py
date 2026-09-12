import streamlit as st

from ai_agent import get_response_from_ai_agent


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="LangGraph Agent UI",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🤖 Agentra")

st.write(
    "Create and interact with AI agents using LangGraph."
)


# -----------------------------
# System prompt
# -----------------------------

system_prompt = st.text_area(
    "Define your AI Agent:",
    height=100,
    placeholder=(
        "Example: Act as an AI chatbot who is smart "
        "and friendly."
    )
)


# -----------------------------
# Models
# -----------------------------

MODEL_NAMES_GROQ = [
    "openai/gpt-oss-120b"
]

MODEL_NAMES_OPENAI = [
    "gpt-4o-mini"
]


# -----------------------------
# Provider
# -----------------------------

provider = st.radio(
    "Select Provider:",
    ("Groq", "OpenAI")
)


# -----------------------------
# Model
# -----------------------------

if provider == "Groq":

    selected_model = st.selectbox(
        "Select Groq Model:",
        MODEL_NAMES_GROQ
    )

else:

    selected_model = st.selectbox(
        "Select OpenAI Model:",
        MODEL_NAMES_OPENAI
    )


# -----------------------------
# Web search
# -----------------------------

allow_web_search = st.checkbox(
    "Allow Web Search"
)


# -----------------------------
# User query
# -----------------------------

user_query = st.text_area(
    "Enter your query:",
    height=150,
    placeholder="Ask Anything!"
)


# -----------------------------
# Ask button
# -----------------------------

if st.button("Ask Agent!", type="primary"):

    if not user_query.strip():

        st.warning("Please enter a query.")

    else:

        try:

            with st.spinner("AI Agent is thinking..."):

                response = get_response_from_ai_agent(
                    llm_id=selected_model,
                    query=[user_query],
                    allow_search=allow_web_search,
                    system_prompt=system_prompt,
                    provider=provider
                )


            st.subheader("Agent Response")

            st.markdown(response)


        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )