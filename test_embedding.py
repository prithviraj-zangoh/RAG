from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Employyes receive 20 paid vacays."

vector = model.encode(text)

print (vector[:2])