from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(path='../inputs/books', glob='*.pdf', loader_cls=PyPDFLoader)

# docs = loader.load()
# print(len(docs))
# print('-'*100)
# print(docs[0].page_content)
# print('-'*100)
# print(docs[0].metadata)


docs = loader.lazy_load()

for d in docs:
    print(d.metadata)


