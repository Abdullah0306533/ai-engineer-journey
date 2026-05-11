from transformers import pipeline

urdu_sentiment = pipeline("text-classification", "cardiffnlp/twitter-xlm-roberta-base-sentiment", device=0)
data = [
    "yeh bohat bura hai",  # This is very bad
    "yeh bohat acha hai",  # This is very good
    "This is amazing",
    "This is terrible"
]
result = urdu_sentiment(data)
print(result)
