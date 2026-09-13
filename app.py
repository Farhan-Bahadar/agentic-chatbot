import streamlit as st
from ai_agent import get_response_from_ai_agent

st.set_page_config(
    page_title="Agentra — AI Agent Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# AGENTRA NOVA UI
# Palette:
#   Midnight #0B1020
#   Indigo   #635BFF
#   Cyan     #22D3EE
#   Violet   #8B5CF6
#   Surface  #111827
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #F5F7FB;
    --surface: #FFFFFF;
    --surface-2: #F8FAFC;
    --navy: #0B1020;
    --navy-2: #111827;
    --indigo: #635BFF;
    --violet: #8B5CF6;
    --cyan: #22D3EE;
    --text: #111827;
    --muted: #6B7280;
    --line: #E5E7EB;
    --success: #10B981;
    --shadow: 0 14px 40px rgba(15, 23, 42, .07);
}

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 85% 4%, rgba(99,91,255,.09), transparent 25%),
        radial-gradient(circle at 55% 25%, rgba(34,211,238,.055), transparent 22%),
        var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 1500px;
    padding: 1.1rem 1.8rem 3rem;
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: var(--navy);
    border-right: 1px solid rgba(255,255,255,.05);
}

section[data-testid="stSidebar"] > div {
    padding: 1.35rem .95rem;
}

.brand-wrap {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 3px;
}

.brand-mark {
    width: 34px;
    height: 34px;
    border-radius: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 800;
    background: linear-gradient(135deg, var(--indigo), var(--violet));
    box-shadow: 0 8px 24px rgba(99,91,255,.3);
}

.brand {
    color: white;
    font-family: "Space Grotesk", sans-serif;
    font-size: 1.45rem;
    font-weight: 700;
    letter-spacing: -.04em;
}

.brand-sub {
    color: #8E99AD;
    font-size: .72rem;
    margin: 0 0 1.8rem 44px;
}

.nav-title {
    color: #667085;
    text-transform: uppercase;
    letter-spacing: .13em;
    font-size: .62rem;
    font-weight: 700;
    margin: 1.25rem 0 .45rem;
}

section[data-testid="stSidebar"] .stButton > button {
    background: transparent;
    color: #B7C0D0;
    border: 0;
    border-radius: 11px;
    min-height: 39px;
    text-align: left;
    font-size: .82rem;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,.07);
    color: white;
}

.sidebar-agent {
    margin-top: 1.6rem;
    padding: 13px;
    border: 1px solid rgba(255,255,255,.08);
    background: rgba(255,255,255,.035);
    border-radius: 15px;
}

.sidebar-agent-title {
    color: #D7DCE6;
    font-size: .75rem;
    font-weight: 700;
}

.sidebar-agent-text {
    color: #7F899B;
    font-size: .66rem;
    line-height: 1.45;
    margin-top: 4px;
}

.sidebar-footer {
    color: #687386;
    font-size: .65rem;
    margin-top: 1rem;
}

/* ---------- Header ---------- */
.top-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.eyebrow {
    color: var(--indigo);
    text-transform: uppercase;
    letter-spacing: .14em;
    font-size: .67rem;
    font-weight: 800;
}

h1 {
    font-family: "Space Grotesk", sans-serif !important;
    color: var(--text) !important;
    font-size: 2.55rem !important;
    letter-spacing: -.06em !important;
    margin: .08rem 0 .25rem !important;
}

.hero-copy {
    color: var(--muted);
    max-width: 760px;
    line-height: 1.55;
    font-size: .9rem;
}

.status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    border: 1px solid #D1FAE5;
    background: #ECFDF5;
    color: #047857;
    border-radius: 999px;
    padding: 7px 12px;
    font-size: .73rem;
    font-weight: 700;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--success);
    box-shadow: 0 0 0 4px rgba(16,185,129,.12);
}

/* ---------- Section ---------- */
.section-label {
    font-family: "Space Grotesk", sans-serif;
    color: var(--text);
    font-weight: 700;
    font-size: .98rem;
}

.section-desc {
    color: var(--muted);
    font-size: .74rem;
    margin: 2px 0 10px;
}

/* ---------- Template cards ---------- */
.template-card {
    background: rgba(255,255,255,.88);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 13px;
    min-height: 82px;
    box-shadow: 0 5px 20px rgba(15,23,42,.035);
}

.template-card:hover {
    border-color: #C7D2FE;
}

.template-icon {
    font-size: 1.08rem;
    margin-bottom: 5px;
}

.template-name {
    color: var(--text);
    font-weight: 700;
    font-size: .8rem;
}

.template-desc {
    color: var(--muted);
    font-size: .63rem;
    margin-top: 2px;
}

/* ---------- Main cards ---------- */
.ui-card {
    background: rgba(255,255,255,.94);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 1.15rem;
    box-shadow: var(--shadow);
}

.card-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.card-title {
    font-family: "Space Grotesk", sans-serif;
    color: var(--text);
    font-size: 1rem;
    font-weight: 700;
}

.card-desc {
    color: var(--muted);
    font-size: .72rem;
    margin: 2px 0 12px;
}

.badge {
    color: var(--indigo);
    background: #EEF2FF;
    border: 1px solid #E0E7FF;
    padding: 5px 8px;
    border-radius: 999px;
    font-size: .61rem;
    font-weight: 700;
}

/* ---------- Widgets ---------- */
.stTextArea textarea,
.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    background: white !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 12px !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus,
.stSelectbox div[data-baseweb="select"]:focus-within {
    border-color: #A5B4FC !important;
    box-shadow: 0 0 0 3px rgba(99,91,255,.09) !important;
}

.stButton > button {
    background: white;
    color: var(--text);
    border: 1px solid var(--line);
    border-radius: 11px;
    min-height: 41px;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #A5B4FC;
    color: var(--indigo);
    background: #FAFAFF;
}

.provider-selected > div > button {
    border-color: var(--indigo) !important;
    color: var(--indigo) !important;
    background: #F4F3FF !important;
}

.run-wrap > div > button {
    background: linear-gradient(135deg, var(--indigo), var(--violet)) !important;
    color: white !important;
    border: 0 !important;
    min-height: 49px;
    font-size: .88rem;
    box-shadow: 0 10px 24px rgba(99,91,255,.22);
}

.run-wrap > div > button:hover {
    color: white !important;
    background: linear-gradient(135deg, #554CEB, #7C4FEA) !important;
    transform: translateY(-1px);
}

.new-chat > div > button {
    background: var(--navy) !important;
    color: white !important;
    border: 0 !important;
    min-height: 42px;
}

.new-chat > div > button:hover {
    color: white !important;
    background: #171E31 !important;
}

.stToggle > label {
    color: var(--text) !important;
}

/* ---------- Model mini stats ---------- */
.mini-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 10px;
}

.mini-stat {
    border: 1px solid var(--line);
    border-radius: 11px;
    padding: 9px;
    background: var(--surface-2);
}

.mini-label {
    color: var(--muted);
    font-size: .6rem;
}

.mini-value {
    color: var(--text);
    font-size: .72rem;
    font-weight: 700;
    margin-top: 2px;
}

/* ---------- Activity ---------- */
.activity-card {
    background: var(--navy);
    border-radius: 19px;
    padding: 15px 17px;
    box-shadow: 0 14px 35px rgba(11,16,32,.12);
}

.activity-title {
    color: white;
    font-family: "Space Grotesk", sans-serif;
    font-weight: 700;
    font-size: .9rem;
}

.activity-desc {
    color: #8993A6;
    font-size: .67rem;
    margin: 2px 0 12px;
}

.activity-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.activity-step {
    color: #8791A4;
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 999px;
    padding: 7px 10px;
    font-size: .65rem;
}

.activity-active {
    color: white;
    background: rgba(99,91,255,.22);
    border-color: rgba(99,91,255,.45);
}

/* ---------- Response ---------- */
.response-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 19px;
    box-shadow: var(--shadow);
    overflow: hidden;
}

.response-head {
    padding: 12px 15px;
    border-bottom: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.response-body {
    padding: 15px;
    line-height: 1.65;
    font-size: .88rem;
}

.ai-chip {
    color: #4F46E5;
    background: #EEF2FF;
    border-radius: 999px;
    padding: 5px 8px;
    font-size: .62rem;
    font-weight: 700;
}

.source-pill {
    display: inline-block;
    color: #4338CA;
    background: #EEF2FF;
    border: 1px solid #E0E7FF;
    border-radius: 999px;
    padding: 5px 9px;
    margin: 3px;
    font-size: .62rem;
}

.empty-response {
    border: 1px dashed #CBD5E1;
    background: #FAFBFC;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    color: var(--muted);
    font-size: .78rem;
}

.footer {
    color: #98A2B3;
    text-align: center;
    font-size: .64rem;
    padding: 1.25rem 0;
}

.stAlert {
    border-radius: 12px !important;
}

/* Hide Streamlit menu/footer chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

@media (max-width: 900px) {
    .block-container { padding: 1rem; }
    h1 { font-size: 2.1rem !important; }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# Session state
# ============================================================
defaults = {
    "system_prompt": (
        "You are Agentra, a smart, helpful and accurate AI assistant. "
        "Answer clearly and directly. Use web search when it is enabled and useful."
    ),
    "provider": "Groq",
    "model": "openai/gpt-oss-120b",
    "allow_search": True,
    "query": "",
    "result": None,
    "selected_template": "Custom",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# Template presets
# ============================================================
template_prompts = {
    "Tutor": (
        "You are an expert tutor. Explain difficult concepts in simple language, "
        "use examples, and guide the learner step by step."
    ),
    "Researcher": (
        "You are a research assistant. Find useful information, compare evidence, "
        "summarize findings clearly, and cite web sources when available."
    ),
    "Coder": (
        "You are a senior software engineer. Write clean, practical code, explain "
        "important decisions, and help debug errors step by step."
    ),
    "News Analyst": (
        "You are a news analyst. Use current web information when available, "
        "compare important developments, and clearly separate facts from analysis."
    ),
    "Custom": defaults["system_prompt"],
}


# ============================================================
# Sidebar
# ============================================================
with st.sidebar:
    st.markdown(
        '<div class="brand-wrap"><div class="brand-mark">✦</div>'
        '<div class="brand">Agentra</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="brand-sub">AI Agent Studio</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="nav-title">Workspace</div>', unsafe_allow_html=True)
    st.button("⌂  Dashboard", use_container_width=True)
    st.button("✦  My Agents", use_container_width=True)
    st.button("◷  Chat History", use_container_width=True)

    st.markdown('<div class="nav-title">Tools</div>', unsafe_allow_html=True)
    st.button("⌘  Models", use_container_width=True)
    st.button("⚙  Settings", use_container_width=True)

    st.markdown(
        '<div class="sidebar-agent">'
        '<div class="sidebar-agent-title">Current agent</div>'
        f'<div class="sidebar-agent-text">{st.session_state.selected_template} · '
        f'{st.session_state.provider}</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-footer">Build the AI agent your task needs.</div>',
        unsafe_allow_html=True
    )


# ============================================================
# Header
# ============================================================
header_left, header_right = st.columns([5, 1.15], vertical_alignment="center")

with header_left:
    st.markdown('<div class="eyebrow">Agentra / Studio</div>', unsafe_allow_html=True)
    st.markdown("# Build your AI agent")
    st.markdown(
        '<div class="hero-copy">Create a specialized agent, connect the tools it needs, '
        'and run real tasks from one focused workspace.</div>',
        unsafe_allow_html=True
    )

with header_right:
    st.markdown(
        '<div class="status"><span class="status-dot"></span> All systems ready</div>',
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown('<div class="new-chat">', unsafe_allow_html=True)
    if st.button("＋  New Chat", use_container_width=True):
        st.session_state.result = None
        st.session_state.query = ""
        st.session_state.selected_template = "Custom"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")


# ============================================================
# Templates
# ============================================================
st.markdown('<div class="section-label">Start with a template</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-desc">Pick a role to instantly configure your agent.</div>',
    unsafe_allow_html=True
)

templates = [
    ("🎓", "Tutor", "Learn & explain"),
    ("🔎", "Researcher", "Search & synthesize"),
    ("💻", "Coder", "Build & debug"),
    ("📰", "News Analyst", "Track current events"),
    ("✦", "Custom", "Define your own"),
]

cols = st.columns(5)
for col, (icon, name, desc) in zip(cols, templates):
    with col:
        if st.button(f"{icon}  {name}", key=f"template_{name}", use_container_width=True):
            st.session_state.selected_template = name
            st.session_state.system_prompt = template_prompts[name]
            if name == "News Analyst":
                st.session_state.allow_search = True
            st.rerun()

        st.markdown(
            f'<div class="template-card">'
            f'<div class="template-icon">{icon}</div>'
            f'<div class="template-name">{name}</div>'
            f'<div class="template-desc">{desc}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

st.write("")


# ============================================================
# Configuration + Ask Agent
# ============================================================
config_col, ask_col = st.columns([1, 1.15], gap="large")

with config_col:
    st.markdown(
        '<div class="ui-card">'
        '<div class="card-head"><div class="card-title">Configure Agent</div>'
        f'<div class="badge">{st.session_state.selected_template}</div></div>'
        '<div class="card-desc">Set the agent personality, model and available tools.</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "System Prompt",
        key="system_prompt",
        height=145,
        placeholder="Define what your agent should do..."
    )

    st.markdown("**AI Provider**")
    p1, p2 = st.columns(2)

    with p1:
        st.markdown(
            '<div class="provider-selected">' if st.session_state.provider == "Groq" else "",
            unsafe_allow_html=True
        )
        if st.button("⚡  Groq", use_container_width=True):
            st.session_state.provider = "Groq"
            st.session_state.model = "openai/gpt-oss-120b"
            st.rerun()
        if st.session_state.provider == "Groq":
            st.markdown("</div>", unsafe_allow_html=True)

    with p2:
        st.markdown(
            '<div class="provider-selected">' if st.session_state.provider == "OpenRouter" else "",
            unsafe_allow_html=True
        )
        if st.button("◎  OpenRouter", use_container_width=True):
            st.session_state.provider = "OpenRouter"
            st.session_state.model = "openrouter/free"
            st.rerun()
        if st.session_state.provider == "OpenRouter":
            st.markdown("</div>", unsafe_allow_html=True)

    models = (
        ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
        if st.session_state.provider == "Groq"
        else ["openrouter/free"]
    )

    if st.session_state.model not in models:
        st.session_state.model = models[0]

    st.selectbox("Model", models, key="model")
    st.toggle("🌐  Web Search", key="allow_search")

    st.markdown(
        f'<div class="mini-grid">'
        f'<div class="mini-stat"><div class="mini-label">Provider</div>'
        f'<div class="mini-value">{st.session_state.provider}</div></div>'
        f'<div class="mini-stat"><div class="mini-label">Tools</div>'
        f'<div class="mini-value">{"Tavily Search" if st.session_state.allow_search else "None"}</div></div>'
        f'</div></div>',
        unsafe_allow_html=True
    )


with ask_col:
    st.markdown(
        '<div class="ui-card">'
        '<div class="card-head"><div class="card-title">Ask Agent</div>'
        '<div class="badge">Ready to run</div></div>'
        '<div class="card-desc">Describe the task. Your configured agent will handle the rest.</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Query",
        key="query",
        height=190,
        placeholder=(
            "What would you like your agent to do?\n\n"
            "Example: Research the latest AI trends and give me a concise "
            "summary with the most important developments."
        ),
        label_visibility="collapsed"
    )

    st.markdown('<div class="run-wrap">', unsafe_allow_html=True)
    run = st.button("✦  Run Agent", use_container_width=True)
    st.markdown("</div></div>", unsafe_allow_html=True)


# ============================================================
# Run agent
# ============================================================
if run:
    if not st.session_state.query.strip():
        st.warning("Enter a task or question before running the agent.")
    else:
        with st.spinner("Agentra is reasoning through your task..."):
            try:
                st.session_state.result = get_response_from_ai_agent(
                    llm_id=st.session_state.model,
                    query=st.session_state.query.strip(),
                    allow_search=st.session_state.allow_search,
                    system_prompt=st.session_state.system_prompt.strip(),
                    provider=st.session_state.provider,
                )
            except Exception as e:
                st.session_state.result = {
                    "response": f"Agent error: {e}",
                    "sources": [],
                    "error": True,
                }


# ============================================================
# Activity
# ============================================================
st.write("")
st.markdown(
    '<div class="activity-card">'
    '<div class="activity-title">Agent Activity</div>'
    '<div class="activity-desc">Your request moves through these stages when the agent runs.</div>'
    '<div class="activity-row">'
    '<span class="activity-step activity-active">01 · Processing</span>'
    f'<span class="activity-step">02 · {"Searching" if st.session_state.allow_search else "No Search"}</span>'
    '<span class="activity-step">03 · Analyzing</span>'
    '<span class="activity-step">04 · Generating</span>'
    '</div></div>',
    unsafe_allow_html=True
)


# ============================================================
# Response
# ============================================================
st.write("")
response_title, response_status = st.columns([4, 1], vertical_alignment="center")

with response_title:
    st.markdown('<div class="section-label">Agent Response</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-desc">The final answer from your configured agent.</div>',
        unsafe_allow_html=True
    )

with response_status:
    if st.session_state.result:
        st.markdown(
            '<div style="text-align:right"><span class="ai-chip">✦ Generated</span></div>',
            unsafe_allow_html=True
        )

if st.session_state.result:
    result = st.session_state.result
    response = result.get("response", "") if isinstance(result, dict) else str(result)
    sources = result.get("sources", []) if isinstance(result, dict) else []

    st.markdown(
        '<div class="response-card">'
        '<div class="response-head"><b>Agentra</b>'
        '<span class="ai-chip">AI OUTPUT</span></div>'
        '<div class="response-body">',
        unsafe_allow_html=True
    )
    st.markdown(response)
    st.markdown("</div></div>", unsafe_allow_html=True)

    if sources:
        st.write("")
        st.markdown("**Web Sources**")
        for source in sources:
            st.markdown(
                f'<span class="source-pill">↗ {source}</span>',
                unsafe_allow_html=True
            )
else:
    st.markdown(
        '<div class="empty-response">'
        '<div style="font-size:1.35rem;margin-bottom:6px">✦</div>'
        '<b>Nothing here yet</b><br>'
        'Configure your agent above, enter a task, and run it to see the result.'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="footer">Agentra · AI Agent Studio · LangChain · LangGraph · Groq · OpenRouter · Tavily</div>',
    unsafe_allow_html=True
)
