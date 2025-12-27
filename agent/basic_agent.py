from langchain_community.tools import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub

# Step-1: Create/Define Tool
search_tool = DuckDuckGoSearchRun()

# Step-2: Create LLM
llm = ChatOllama(model='llama3.1')

# Step-3: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")

# Step-4: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# Step-5: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

# Step -6: Invoke
# response = agent_executor.invoke({"input": "3 ways to reach Goa from Delhi"})
response = agent_executor.invoke({"input": "tell me the population of capital of India"})

print(response)

