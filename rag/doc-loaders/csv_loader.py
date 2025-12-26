from langchain_community.document_loaders import CSVLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = CSVLoader(file_path='../inputs/country_full.csv')

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

model = ChatOllama(model='llama3')

template = PromptTemplate(
    template="""
    What is the country-code for the given country - {country} from the attached text - {text}
    """,
    input_variables=['country', 'text'],
    validate_template=True
)

prompt = template.invoke({'country': 'Belgium','text': docs[21]})

print(prompt)

parser = StrOutputParser()

chain = template | model | parser

response = chain.invoke({'country': 'Belgium', 'text': docs[21]})

print(response)