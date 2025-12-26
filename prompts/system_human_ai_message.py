from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from pyexpat.errors import messages

model = ChatOllama(model="llama3")

messages = [
    SystemMessage(content="You are an expert in reviewing the english essays and rate them on a scale of 5"),
    HumanMessage(content="Cricket is a bat-and-ball outdoor team sport played by two teams of eleven players on a large field with a rectangular pitch at the center. The objective is to score more runs than the opposing team by hitting a ball and running between wickets. Originating in England, it's now globally popular, especially in former British colonies like India, where it's considered a cultural phenomenon fostering unity, discipline, and passion for the game. Key elements of the game include batting, bowling, and fielding, with various formats such as Test matches, One Day Internationals (ODIs), and Twenty20 (T20).")
]


result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
