import requests

BASE_URL = "http://localhost:8080"

try:
    r = requests.get(f"{BASE_URL}/api/v1/index/list", timeout=5)
    print("Status Code:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print("Error connecting to Endee:", e)
