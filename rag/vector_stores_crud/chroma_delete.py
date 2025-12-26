from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# Each DocId from create
# ['eff995a4-720d-4a53-9c7a-bdf4d246b7bc',
# '574b0e45-9941-45dd-992a-ffdc66225a23',
# 'd90b58de-48a1-4c1a-93e3-1c5f2cda40b1',
# '3fa89e8e-6255-40cb-af1e-0e3fc3cf5d12',
# 'ee743737-bd1f-4cd5-9162-033b5d5bb381']

vector_store = Chroma(
    embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

print(vector_store.get(include=['embeddings','documents', 'metadatas']))

# delete document for Viral Kohli, copy the doc id from previous run
vector_store.delete(ids=['eff995a4-720d-4a53-9c7a-bdf4d246b7bc'])

print('-'*100)
print(vector_store.get(include=['embeddings','documents', 'metadatas']))