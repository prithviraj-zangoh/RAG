from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_vectorstore():
    embedding_func = HuggingFaceEmbeddings("sentence-transformers/all-MiniLM-L6-v2")

    return Chroma (
        persist_directory="./chroma.db",
        embedding_function=embedding_func
    )

