from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent


load_dotenv()

model = ChatOpenAI(model="gpt-4")

search = TavilySearchResults(max_results=2)
tools = [search]

agent_executor = create_react_agent(model, tools)

if __name__ == '__main__':
    response = agent_executor.invoke({"messages" : [HumanMessage(content="What is the weather in İstanbul now?")]})
    print(response)
