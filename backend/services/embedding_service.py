import requests
import os

# Explicit feature-extraction URL taake Hugging Face confuse na ho
API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def get_embedding(text: str):
    hf_key = os.environ.get('HF_API_KEY')
    
    if not hf_key:
        raise ValueError("Render mein HF_API_KEY nahi mil rahi!")

    headers = {"Authorization": f"Bearer {hf_key}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Hugging Face Error: {response.text}")