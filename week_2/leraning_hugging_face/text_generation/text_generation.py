from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2",
    device=0
)

result = generator(
    text_inputs="Artificial intelligence will transform",
    max_length=50
)

print(result)