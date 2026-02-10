import requests
from embed import embed_texts

BASE_URL = "http://localhost:8080"
INDEX_NAME = "default"   # Endee-managed default index

texts = [
    "Python is a programming language",
    "Vector databases store embeddings",
    "Endee is a high performance vector database",
    "Artificial intelligence learns from data",
    "Databases store and retrieve information"
]

vectors = embed_texts(texts)

payload = {
    "items": [
        {
            "id": str(i),
            "vector": vectors[i].tolist(),
            "metadata": {
                "text": texts[i]
            }
        }
        for i in range(len(texts))
    ]
}

response = requests.post(
    f"{BASE_URL}/api/v1/index/{INDEX_NAME}/insert",
    json=payload,
    timeout=20
)

print("Status:", response.status_code)
print("Response:", response.text)
