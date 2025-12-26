from langchain_community.llms.ollama import Ollama

llm = Ollama(model='llama2:7b')

response = llm.invoke("What is the capital of India?")

print(f"Response: {response}")