from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

model = ChatOllama(model='llama3.1')

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'topic': 'Cricket'})

print(response)

print(chain.get_graph().draw_ascii())