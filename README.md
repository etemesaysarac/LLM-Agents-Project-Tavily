LLM Agents Project — ReAct Web-Search Agent (LangChain + Tavily + OpenAI)
~~
~~

A sharp, production-style ReAct agent that understands your question, decides when to search the web, and returns a clear, sourced answer.
It’s built for observability and extensibility: you can watch each tool call, tweak prompts, and add new tools in minutes.

Table of Contents

What This Project Does

Screenshots

How It Works

Tech Stack

Project Structure

Getting Started

Run the Agent

Troubleshooting

Roadmap

License

What This Project Does

🧠 ReAct Agent (Reason + Act): Uses an LLM to plan actions and call tools.

🌐 Live Web Search (Tavily): Pulls fresh information when the model decides it needs it.

🧾 Step-by-Step Transparency: Every tool call (input + observation) is visible in the logs/UI.

🗣️ Conversation Awareness: Can be run with session-based history to remember context across turns.

🧩 Pluggable Tools: Add more tools (calculator, Wikipedia, databases) with minimal code.

Screenshots

Place images under ./assets/ as 1.png, 2.png, 3.png, 4.png (filenames below). They’ll render automatically on GitHub.

<p align="center"> <img src="./assets/1.png" alt="Agent workflow graph" width="720"> </p> <p align="center"><em>Figure 1 — Agent execution graph.</em></p> <p align="center"> <img src="./assets/2.png" alt="Early agent run with weather query" width="720"> </p> <p align="center"><em>Figure 2 — Early-stage run: the agent decides to perform a weather check and responds with up-to-date information.</em></p> <p align="center"> <img src="./assets/3.png" alt="Conversation memory demonstration" width="720"> </p> <p align="center"><em>Figure 3 — With memory enabled, the agent recalls prior turns and reasons over them.</em></p> <p align="center"> <img src="./assets/4.png" alt="Final agent behavior and behind-the-scenes view" width="1000"> </p> <p align="center"><em>Figure 4 — Final state: a behind-the-scenes view showing how the agent orchestrates tools under the hood.</em></p>
How It Works

Prompting (ReAct pattern):
A ReAct prompt guides the model to think first, then act via tools, and finally answer. We use the public ReAct template from langchain-hub.

Tooling (Tavily Web Search):
The agent can call Tavily to search the web when its internal reasoning decides that external information is needed.

Orchestration (AgentExecutor):
LangChain’s AgentExecutor glues the LLM + tools + prompt together and returns both the final answer and intermediate steps (so you can audit what happened).

Memory (optional, session-based):
You can wrap the executor with a session history layer to retain multi-turn context. This keeps the agent “aware” of prior messages without hardcoding state handling.

Note: There’s also a LangGraph path with SQLite checkpointing for persistent, resumable graphs. Choose the approach that fits your deployment style.

Tech Stack

LLM: ChatOpenAI (model: gpt-4o-mini, configurable)

Agent: ReAct (create_react_agent from LangChain)

Search Tool: langchain-tavily (TavilySearch)

Prompt Source: langchain-hub (hwchase17/react)

Env Management: python-dotenv

Project Structure
.
├─ main.py
├─ requirements.txt
├─ .env.example
└─ assets/
   ├─ 1.png   # Agent workflow graph
   ├─ 2.png   # Early weather query run
   ├─ 3.png   # Memory demonstration
   └─ 4.png   # Final behind-the-scenes view

Getting Started
1) Clone & create a virtual environment
git clone <your-repo-url>
cd <your-repo-folder>

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

2) Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

3) Configure API keys

Create a .env file in the repo root:

OPENAI_API_KEY=sk-.................................
TAVILY_API_KEY=tvly-...............................


(Alternatively set them as environment variables in your shell/session.)

Run the Agent
python main.py


Type your question at the > prompt.

Watch the agent plan, search, and answer.

If verbose logging is enabled, you’ll also see the reasoning path, tool inputs, and observations.

Troubleshooting

The api_key client option must be set ...
Ensure .env exists and load_dotenv() is called before creating the client. Keys must be tırnaksız (no quotes).

Deprecation warnings about memory (LangChain 0.3+):
Prefer session-based history wrappers (RunnableWithMessageHistory) instead of legacy ConversationBufferMemory, or use LangGraph + SQLite checkpointing.

“Tool list” mistakes (tuple has no name / agent can’t render tools):
create_react_agent expects a list of tools (e.g., tools = [web_search]), not a single object.

Old Tavily imports (langchain_community.tools.tavily_search):
Use the modern package: langchain-tavily (from langchain_tavily import TavilySearch).

Package version conflicts:
Run pip install -r requirements.txt inside a clean venv. If a single package version fails to resolve on your machine, pin/adjust just that line and reinstall.

Roadmap

Add more tools (Calculator, Wikipedia, custom RAG)

Streamed token output for live typing UX

Web UI (FastAPI + simple chat front-end)

Dockerfile & CI/CD

Source citations inline in answers

License

MIT — feel free to use, modify, and ship.

Credits

Built with ❤️ using LangChain, Tavily, and OpenAI.
Screenshots captured from the agent’s debug views to illustrate real decision flows.