from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
# from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
memory = SqliteSaver.from_conn_string(":memory:")
search = TavilySearch(max_results=2, include_answer=True, include_raw_content=True)
prompt = hub.pull("hwchase17/react")
tools = [search]
agent = create_react_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools= tools, verbose = True, checkpoint=memory)

config = {"configurable" : {"thread_id" : "Easyso2025"}}

if __name__ == "__main__":
    chat_history = []
    response = []
    while True:
        user_input = input(" > ")
        for chunk in agent_executor.stream({"input" : user_input, "chat_history" : "\n".join(chat_history)}, config=config):
            if "text" in chunk:
                print(chunk["text"], end="")
                response.append(chunk["text"])
        chat_history.append(f"AI: {"".join(response)}")