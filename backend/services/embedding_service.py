import requests
import os
import time

API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def get_embedding(text: str):
    hf_key = os.environ.get('HF_API_KEY')
    
    if not hf_key:
        raise ValueError("Render mein HF_API_KEY nahi mil rahi!")

    headers = {"Authorization": f"Bearer {hf_key}"}
    
    # Render ke saste network se bachne ke liye 3 dafa auto-try karega
    for i in range(3):
        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": text})
            
            if response.status_code == 200:
                return response.json()
            else:
                raise ValueError(f"Hugging Face Error: {response.text}")
                
        except requests.exceptions.ConnectionError:
            # Agar network error aaye toh 2 second ruk kar wapas try kare
            if i == 2: # Agar teesri dafa bhi fail ho toh phir error de
                raise ValueError("Render ka network Hugging Face tak nahi pohanch raha (DNS Error).")
            time.sleep(2)