import requests
import os

# Naya router URL jo Render block nahi karta aur exact vector (feature-extraction) nikalta hai
API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"

def get_embedding(text: str):
    hf_key = os.environ.get('HF_API_KEY')
    
    if not hf_key:
        raise ValueError("Render mein HF_API_KEY nahi mil rahi!")

    headers = {"Authorization": f"Bearer {hf_key}"}
    
    # Ab loop ki zaroorat nahi kyunke router URL direct connect hota hai
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Hugging Face Error: {response.text}")