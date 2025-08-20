from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver  # kalıcı bellek (SQLite)

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
tavily = TavilySearch(max_results=2, include_answer=True, include_raw_content=True)
tools = [tavily]

# DİKKAT: context manager şart!  :contentReference[oaicite:3]{index=3}
with SqliteSaver.from_conn_string("checkpoints.sqlite") as checkpointer:
    agent = create_react_agent(llm, tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "abc123"}}

    if __name__ == "__main__":
        while True:
            user_input = input(">")
            for step in agent.stream({"messages": user_input}, config, stream_mode="values"):
                step["messages"][-1].pretty_print()
                print("----")
