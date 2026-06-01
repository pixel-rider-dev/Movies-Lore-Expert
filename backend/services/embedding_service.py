import requests
import os

# Render par load_dotenv ki zaroorat nahi hoti, is liye hum usay hata rahe hain
API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"

# Yeh line Render ke environment se direct key nikal layegi
hf_key = os.environ.get('HF_API_KEY')
headers = {"Authorization": f"Bearer {hf_key}"}

def get_embedding(text: str):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Embedding Error: {response.text}")
        return []