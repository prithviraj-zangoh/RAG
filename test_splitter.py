from app.loaders import load_documents

from langchain_text_splitters import RecursiveCharacterTextSplitter

docs = load_documents()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
)

chunks = splitter.split_documents(docs)

print("Total Chunks", len(chunks))