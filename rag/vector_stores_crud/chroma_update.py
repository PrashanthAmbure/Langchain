from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

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

# update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)
# Copy the document id from the previous create to update
vector_store.update_document(document_id='eff995a4-720d-4a53-9c7a-bdf4d246b7bc', document=updated_doc1)

# view documents
print('-'*100)
print(vector_store.get(include=['embeddings','documents', 'metadatas']))