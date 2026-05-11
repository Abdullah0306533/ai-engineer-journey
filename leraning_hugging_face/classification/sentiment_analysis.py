from transformers import pipeline

# Not choosing the model
sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love building AI systems",
        "This code is frustrating and broken",
        "The weather is okay"]
output=sentiment_pipeline(data)
print(output)

# Choosing the specific model
specific_model_sentiment = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
specific_output = specific_model_sentiment(data)
print(specific_output)
sentiment_pipeline = pipeline("sentiment-analysis", device=0)
print(sentiment_pipeline.model.device)
