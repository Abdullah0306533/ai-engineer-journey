import chromadb as db

client = db.PersistentClient(path=r"C:\Users\Pc\Desktop")

collection = client.get_or_create_collection(name="data")

# Add documents (correct method)
collection.add(
    ids=['1','2','3','4','5'],
    documents=[
        "The movie Titanic is a romantic disaster film about the sinking of the Titanic ship.",
        "Tesla produces electric cars known for innovation and performance.",
        "The Mughal Empire ruled South Asia and built the Taj Mahal.",
        "Football is the most popular sport in the world played with a round ball.",
        "Biryani is a famous dish made with rice, spices, and meat."
    ]
)
print(collection.count())

collection.upsert(
    ids=['1'],
    documents=['I have successfully edited doc wit id 1']
)
collection.upsert(
    ids=['6'],
    documents=['I have successfully added doc wit id 6']
)
collection.delete(
    ids=['6']
)
print(collection.count())
# Retrieve single items
print(collection.get(ids=['1']))
print(collection.get(ids=['2']))
print(collection.get(ids=['6']))
print(collection.count())