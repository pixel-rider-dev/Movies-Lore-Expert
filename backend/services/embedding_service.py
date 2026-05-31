import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Hugging Face Free API URL exact same model ke liye
API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"

# Token aap ki .env file se aayega
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def get_embedding(text: str):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Embedding Error: {response.text}")
        return []