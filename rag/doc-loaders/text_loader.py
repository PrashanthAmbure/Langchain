from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model='llama3')

template = PromptTemplate(
    template="""
    Write a detailed report on {topic}
    """,
    validate_template=True,
    input_variables=['topic']
)

parser = StrOutputParser()

loader = TextLoader('../inputs/cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs)

print("-"*100)
print(type(docs))

print("-"*100)
print(len(docs))

print("-"*100)
print(docs[0])

print("-"*100)
print(type(docs[0]))

print("-"*100)
print(docs[0].page_content)

print("-"*100)
print(docs[0].metadata)

chain = template | model | parser

response = chain.invoke({'topic': docs[0].page_content})

print("-"*100)
print(response)