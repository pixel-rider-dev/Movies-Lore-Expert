import requests
import os

API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"

def get_embedding(text: str):
    # Key ko function ke andar nikalna zaroori hai taake fresh load ho
    hf_key = os.environ.get('HF_API_KEY')
    
    if not hf_key:
        raise ValueError("Render mein HF_API_KEY nahi mil rahi!")

    headers = {"Authorization": f"Bearer {hf_key}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        return response.json()
    else:
        # Ab agar HF fail hua, toh yeh Pinecone tak jane hi nahi dega aur asal wajah batayega
        raise ValueError(f"Hugging Face Error Pakra Gaya: {response.text}")