from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, load_prompt

model = ChatOllama(model="llama3")

template = load_prompt('template.json')

prompt = template.invoke({"lines": 5, "topic": "cricket"})

response = model.invoke(prompt)

print(f"Response: {response.content}")

