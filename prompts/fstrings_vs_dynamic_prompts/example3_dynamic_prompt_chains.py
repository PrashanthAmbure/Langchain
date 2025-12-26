from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model='llama3')

template = PromptTemplate(
    template="""
    Summarize on {topic}
    """,
    input_variables=['topic'],
    validate_template=True
)

# prompt = template.invoke({"topic": "machine learning"})
# response = model.invoke(prompt)

chain = template | model

response = chain.invoke({"topic": "machine learning"})

print(f"Response: {response.content}")