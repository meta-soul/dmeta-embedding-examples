from langchain.schema import Document
from langchain.vectorstores import VectorStore
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from dotenv import load_dotenv
from typing import List

import pickle

load_dotenv()

index_path = "./vectorstore_douban_movie-1k.pkl"

min_document_len = 10
ret_top_k = 10

with open(index_path, "rb") as f:
    vectorstore = pickle.load(f)
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)

def filter_documents(documents: List[Document]) -> List[Document]:
    return [d for d in documents if len(d.page_content) > min_document_len]


def query_on_index(query):
    retriever = index.vectorstore.as_retriever(search_kwargs={"k": ret_top_k})
    documents = retriever.get_relevant_documents(query)
    documents = filter_documents(documents)
    if len(documents) > ret_top_k:
        documents = documents[0:ret_top_k]
    
    return documents

while True:
    user_query = input("Please enter your query (or type 'exit' to quit): ")

    if user_query.lower() == 'exit':
        break

    results = query_on_index(user_query)

    for doc in results:
        print(doc.page_content)
    print("\n") 
