from app.loaders import load_documents

docs = load_documents()

print(len(docs))

for doc in docs:
    print("=" * 40)
    print(doc.page_content)
