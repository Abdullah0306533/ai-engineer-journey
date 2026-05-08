from transformers import pipeline

classifier = pipeline("zero-shot-classification", device=0)

sentence = "The patient has elevated glucose and high blood pressure"
labels = ["diabetes", "hypertension", "stroke", "fracture"]
result = classifier(sentence, candidate_labels=labels)

for label, score in zip(result['labels'], result['scores']):
    print(f"{label}: {score:.4f}")