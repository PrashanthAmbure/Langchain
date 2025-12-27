from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub
import requests

API_KEY=""

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather(city: str) -> str:
    """
    Given a city name, fetch the current weather conditions
    :param city:
    :return:
    """
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    return requests.get(url).json()

llm = ChatOllama(model='llama3.1')

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather],
    verbose=True
)

response = agent_executor.invoke({'input': 'Find the capital of Telangana, then find its current weather condition?'})

print(response)