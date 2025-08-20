from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


load_dotenv()

model = ChatOpenAI(model="gpt-4")

search = TavilySearchResults(max_results=2)
tools = [search]

model_with_tools = model.bind_tools(tools)

if __name__ == '__main__':
    response = model_with_tools.invoke([HumanMessage(content="What's the weather in istanbul?")])
    print(f"ContentString: {response.content}")
    print(f"ToolCalls: {response.tool_calls}")
    #tool called tavily