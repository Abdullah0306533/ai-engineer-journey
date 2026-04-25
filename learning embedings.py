from sentence_transformers import SentenceTransformer
import numpy as np

query = "My blood glucose is too high"

knowledge_base = [
    "Normal fasting glucose is 70-100 mg/dL.",
    "Hemoglobin carries oxygen in red blood cells.",
    "High blood sugar is linked to diabetes.",
    "The liver produces bile for digestion.",
    "Elevated glucose levels require dietary changes."
]

model = SentenceTransformer('all-MiniLM-L6-v2')

query_vec = model.encode(query)
embeddings = model.encode(knowledge_base)


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    magnitude = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / magnitude


# Finding the most similar line

find = list(range(len(knowledge_base)))
for i in range(len(embeddings)):
    find[i] = cosine_similarity(query_vec, embeddings[i])

# Printing Line the most similar
max_prob=max(find)
print(f"Query: {query} Matched Sentence:{knowledge_base[find.index(max_prob)]} {max_prob}")
