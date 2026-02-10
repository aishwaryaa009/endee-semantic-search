import requests

BASE_URL = "http://localhost:8080"
endpoint = f"{BASE_URL}/api/v1/index/create"

payload = {
    "name": "my_vector_index",
    "dimension": 1536,
    "metric": "cosine"
}

response = requests.post(endpoint, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
