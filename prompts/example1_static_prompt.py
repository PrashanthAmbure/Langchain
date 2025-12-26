from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3")

response = model.invoke("Who is the 'God of Cricket'?")

print(f"Response: {response.content}")

