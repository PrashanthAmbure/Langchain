from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

import numpy as np

video_id = "nwkn0hAUz2k" # only the ID, not full URL
ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id)

# is iterable
for snippet in fetched_transcript:
    print(snippet.text)

# Flatten it to plain text
transcript = " ".join(chunk.text for chunk in fetched_transcript)
print(transcript)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = splitter.create_documents([transcript])

print('*'*100)
print(len(chunks))

print('*'*100)
print(chunks[2])

embedding_model = OllamaEmbeddings(model="nomic-embed-text")
vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

print('*'*100)
print(vector_store.index_to_docstore_id)
num_vectors = vector_store.index.ntotal
print("Total vectors in FAISS index:", num_vectors)

# FAISS stores vectors in a flat array internally
vectors = np.array(vector_store.index.reconstruct_n(0, num_vectors))

# Preview first 3 vectors
for i in range(min(5, num_vectors)):
    print(f"\n--- Vector {i+1} ---")
    print("Vector dimensions:", len(vectors[i]))
    print("First 10 values:", vectors[i][:10])


# print(vector_store.get_by_ids(['3c3a294c-a787-465e-ac15-40db707e20b3']))

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatOllama(model='llama3')

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)


# question          = "Is the topic of Christopher discussed in this video? If yes then what was discussed"
# question          = "Is the name Christopher used in this video? If yes then what was discussed"
question          = "Can you please summarize what the user is talking in the video?"
retrieved_docs    = retriever.invoke(question)

print('-'*100)
print(retrieved_docs)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
final_prompt = prompt.invoke({"context": context_text, "question": question})


answer = llm.invoke(final_prompt)
print('*'*100)
print(answer.content)

# Building a chain
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

parallel_chain.invoke('What is docker compose?')

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

print(main_chain.invoke('Can you summarize the video'))