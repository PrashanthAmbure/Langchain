from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="llama3")

template = PromptTemplate(
    template="""
    Explain in {lines} lines about {topic}
    """,
    input_variables=['lines', 'topic'])


prompt = template.invoke({"lines": 5, "topic": "cricket"})
print(prompt)

response = model.invoke(prompt)

print(f"Response: {response.content}")

