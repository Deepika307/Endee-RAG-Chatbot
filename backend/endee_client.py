import requests
from backend.config import ENDEE_URL, INDEX_NAME


API_TOKEN = "mytoken123"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}


def insert_vectors(vectors):
    url = f"{ENDEE_URL}/indexes/{INDEX_NAME}/insert"

    payload = {
        "vectors": vectors
    }

    
    response = requests.put(url, json=payload, headers=HEADERS)

    print("STATUS:", response.status_code)

    try:
        return response.json()
    except:
        return response.text
