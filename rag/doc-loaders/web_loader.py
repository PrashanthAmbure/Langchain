from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model='llama3')

template = PromptTemplate(
    template="""
    Answer the following question \n {question} from the following text - \n {text}
    """,
    input_variables=['question', 'text'],
    validate_template=True)

parser = StrOutputParser()

url='https://www.amazon.in/dp/B0FZT1LXPZ/?_encoding=UTF8&ref_=cct_cg_Budget_2a1&pf_rd_p=659fd536-fa9f-4ede-a098-3d02ba0d1ac1&pf_rd_r=PA75RTRQN5XWHGPYED1C&th=1'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print('-'*100)
print(docs[0].page_content)

chain = template | model | parser

response = chain.invoke({'question': 'What is the product name?', 'text':docs[0].page_content})
print('-'*100)
print(response)