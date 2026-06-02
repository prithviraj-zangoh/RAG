from langchain_community.vectorstores import Chroma

from langchain_huggingface import HuggingFaceEmbeddings

embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_function
)


def retrieve(question):

    results = db.similarity_search_with_score(
        question,
        k=3
    )

    return results

###############

question = (
    "How many vacation days "
    "do employees receive?"
)

results = retrieve(question)

for result in results:

    print("=" * 50)

    print(result.page_content)