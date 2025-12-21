#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults


#open_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=3)

#Step 3 - Setup the AI Agent with search tool functionality

from langgraph.prebuilt import create_react_agent

system_prompt="You are an AI assistant that helps users by answering questions and providing information."

agent=create_react_agent(
    model=groq_llm,
    tools=[search_tool],
    state_modifiers=system_prompt
)


query="tell me about the latest advancements in AI technology"
state={"message": query}
response=agent.invoke(state)
print(response)
