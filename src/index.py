import requests

BASE_URL = "http://localhost:8080"
INDEX_NAME = "demo-index"

def create_index():
    payload = {
        "index_name": INDEX_NAME,
        "dimension": 384,
        "distance_type": "cosine",
        "index_type": "flat",
        "num_shards": 1,
        "num_replicas": 1
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/index/create",
        json=payload,
        timeout=10
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    create_index()
