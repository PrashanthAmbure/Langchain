from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3", temperature=0.5)

response = model.invoke("What is the capital of India?")

print(f'Response: {response}')
print("*"*50)
print(f"Response={response.content}")