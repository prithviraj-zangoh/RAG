from langchain_community.document_loaders import TextLoader

def load_document():
    docs=[]

    files = [
        "data/company_policy.txt"
        "data/vacation_plicy.txt"
        "data/remote_work.txt"
    ]

    for file in files:
        docs.extend(TextLoader(file).load())

    return docs