from click import prompt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
#from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
tavily = TavilySearch(max_results=2, include_answer=True, include_raw_content=True)
tools = [tavily]

prompt = hub.pull("hwchase17/react")

# DİKKAT: context manager şart!  :contentReference[oaicite:3]{index=3}
with SqliteSaver.from_conn_string("checkpoints.sqlite") as checkpointer:
    agent = create_react_agent(llm, tools, prompt)
    config = {"configurable": {"thread_id": "Easyso2025"}}

    if __name__ == "__main__":
        while True:
            user_input = input(">")
            for step in agent.stream({"messages": user_input}, config, stream_mode="values"):
                step["messages"][-1].pretty_print()
                print("----")
