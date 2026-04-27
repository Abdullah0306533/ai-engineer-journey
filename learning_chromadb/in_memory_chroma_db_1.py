import chromadb

chroma_client = chromadb.Client()
# Creating collection to store the data
collection = chroma_client.create_collection(name='medical_knowledge')
collection.add(
    ids=['1', '2', '3', '4', '5'],
    documents=[
        "Prescription",
        "Medical Report",
        "Discharge Summary",
        "Lab Test Report",
        "Medical Certificate"
    ]

)
result=collection.query(
    query_texts=["medicine"],
    n_results=1
)
print(result)