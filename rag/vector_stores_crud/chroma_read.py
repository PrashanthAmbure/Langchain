from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


vector_store = Chroma(
    embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

# search documents
print('-'*100)
print(vector_store.similarity_search(
    query='Who among these are a bowler?',
    k=1
))

# search with similarity score
print('-'*100)
print(vector_store.similarity_search_with_score(
    query='Who among these are a bowler?',
    k=1
))

# meta-data filtering
print('-'*100)
print(vector_store.similarity_search_with_score(
    query="",
    filter={"team": "Chennai Super Kings"}
))