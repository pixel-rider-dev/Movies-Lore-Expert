import requests
import os

# New router URL that Render does not block and extracts the exact vector (feature-extraction)
API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"

def get_embedding(text: str):
    hf_key = os.environ.get('HF_API_KEY')
    
    if not hf_key:
        raise ValueError("HF_API_KEY not found in Render environment!")

    headers = {"Authorization": f"Bearer {hf_key}"}
    
    # Loop is no longer needed because the router URL connects directly
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Hugging Face Error: {response.text}")