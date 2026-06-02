from langchain_community.document_loaders import TextLoader

def load_documents():

    files = [
        "data/employee_handbook.txt",
        "data/remote_work_policy.txt",
        "data/security_policy.txt",
    ]

    docs = []

    for file in files:
        loader = TextLoader(file)
        docs.extend(loader.load())

    return docs