from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model='gemma3:12b')

template1 = PromptTemplate(
    template="""
    Write a detailed report on {topic}
    """,
    validate_template=True,
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="""
    Write a 5 line summary on the following text {llm1_output}
    """,
    validate_template=True,
    input_variables=['llm1_output']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

response = chain.invoke({'topic': 'Black Hole'})

print(f"Response: {response}")