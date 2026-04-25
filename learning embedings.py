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


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    magnitude = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / magnitude


def find_most_similar(_query, _knowledge_base):
    query_vec = model.encode(_query)
    embeddings = model.encode(_knowledge_base)
    # Finding the most similar line
    scores = [cosine_similarity(query_vec, emb) for emb in embeddings]
    highest_score = max(scores)
    index = scores.index(highest_score)
    _result = _knowledge_base[index]
    return _result, highest_score


# Printing Line the most similar
result, score = find_most_similar(query, knowledge_base)
print(f"Best match: {result}")
print(f"Score: {score:.4f}")
