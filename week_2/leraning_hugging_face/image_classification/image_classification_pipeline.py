from transformers import pipeline
classifier = pipeline("image-classification", model="google/vit-base-patch16-224", device=0)
result = classifier(r"C:\Users\Pc\Desktop\download.jpeg")
print(result)
