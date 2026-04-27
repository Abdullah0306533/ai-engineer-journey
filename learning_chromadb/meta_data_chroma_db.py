import chromadb as db

client = db.PersistentClient(path=r"C:\Users\Pc\Desktop")

collections = client.get_or_create_collection(name="practising_meta_data")

collections.upsert(
    ids=["1", "2", "3"],
    documents=[
        "I am Abdullah Butt age 22 and I will become an ai engineer",
        "I am Ali age 22 and I will become an ai engineer",
        "I am Ahmad age 22 and I will become an ai engineer",
    ],
    metadatas=[
        {"name": "Abdullah Butt", "age": 22, "passion": "Ai Engineer"},
        {"name": "Ali", "age": 22, "passion": "Ai Engineer"},
        {"name": "Ahmad", "age": 22, "passion": "Ai Engineer"}]
)

# finding the data
data=collections.query(
    query_texts=["age 22"]
)
print(data)

data_mata_data=collections.query(
    query_texts=["age 22"],
    where={"name":"Abdullah Butt"}
)
print(data_mata_data)