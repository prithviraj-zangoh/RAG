from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")

docs = [
    "Employees receive 20 paid vacations",
    "Employees may work remotely three days per week",
    "Employyes must wear id cards"
]

question = "what should we wear in office"


doc_vectors = model.encode(docs)
question_vectors = model.encode([question])

scores = cosine_similarity([question_vectors[0]], doc_vectors)[0]

for doc, score in zip(docs, scores):
    print (score,doc)
