from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

model  = ChatOllama(model="llama3")

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert"),
#     HumanMessage(content="Explain in simple terms, what is {topic}")
# ])
#
# prompt = chat_template.invoke({"domain": "cricket", "topic": "dusra"})
# print(f"Prompt: {prompt}")

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({"domain": "cricket", "topic": "dusra"})
print(f"Prompt: {prompt}")

response = model.invoke(prompt)

print(f"Response: {response.content}")