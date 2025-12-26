from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("../inputs/ml.pdf")

docs = loader.load()

# print(docs)

print('-'*100)
print(len(docs))

print('-'*100)
print(docs[0].page_content)

print('-'*100)
print(docs[0].metadata)