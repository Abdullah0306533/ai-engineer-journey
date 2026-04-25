from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Patient has high blood sugar.",
    "Glucose level is elevated.",
    "The weather is nice today.",
    "Hemoglobin is below normal range."
]

embeddings = model.encode(sentences)

def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    magnitude = np.linalg.norm(a) * np.linalg.norm(b)
    return dot_product / magnitude

sim_1_2 = cosine_similarity(embeddings[0], embeddings[1])
sim_1_3 = cosine_similarity(embeddings[0], embeddings[2])
sim_1_4 = cosine_similarity(embeddings[0], embeddings[3])

print(f"'High blood sugar' vs 'Glucose elevated': {sim_1_2:.4f}")
print(f"'High blood sugar' vs 'Weather is nice': {sim_1_3:.4f}")
print(f"'High blood sugar' vs 'Hemoglobin low':  {sim_1_4:.4f}")