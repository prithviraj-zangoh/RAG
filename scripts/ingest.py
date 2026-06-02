# from app.loaders import load_documents
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from sentence_transformers import SentenceTransformer


# docs = load_documents()

# splitter = RecursiveCharacterTextSplitter(chunk_size = 100, chunk_overlap = 20)

# chunks = splitter.split_documents(documents=docs)

# print (len(chunks))


# # for i, chunk in enumerate(chunks):

# #     print("\n")
# #     print("=" * 50)

# #     print(f"Chunk {i}")

# #     print(chunk.page_content)

# model = SentenceTransformer("all-MiniLM-L6-v2")

# embeddings = model.encode([chunk.page_content for chunk in chunks])

# print (len(embeddings))


from app.loaders import load_documents
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

docs = load_documents()

splitter = RecursiveCharacterTextSplitter(chunk_size = 100, chunk_overlap=20)
chunks = splitter.split_documents(docs)

embedding_function = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

db = Chroma.from_documents(documents=chunks, embedding=embedding_function, persist_directory="./chroma_db")

print("Ingestion Done", db._collection.count())
