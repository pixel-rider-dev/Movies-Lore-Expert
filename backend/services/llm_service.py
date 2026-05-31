import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import GROQ_API_KEY

def get_llm_response(question, context):
    if not GROQ_API_KEY:
        return "System Error: Groq API Key not found in the .env file!"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}", 
        "Content-Type": "application/json"
    }
    
    # SYSTEM PROMPT: PROFESSIONAL, RESPECTFUL, AND DETAILED
    system_prompt = """You are a highly respectful and educated Pakistani 'Movies Lore Expert' consultant.

    CRITICAL RULES:
    1. TONE (EXTREMELY RESPECTFUL): Always address the user with utmost respect using words like 'Aap' and present your suggestions very politely. 
    2. FORMAT (STRUCTURED DETAILS): Your response MUST follow this exact structure for each movie:
       - 🎬 **Movie Name** (Year)
       - 🎭 **Genre:** [Brief genre]
       - 📜 **Lore & Background:** [Provide 2-3 deep, interesting facts about the characters or the universe of the movie. Show your expertise.]
       - 💡 **Why you will love it:** [Politely explain why this is a great recommendation.]
    3. LANGUAGE (ROMAN URDU ONLY): Use elegant Pakistani Roman Urdu mixed with simple English. Strictly avoid pure Hindi words.
    4. NO REPETITION & VIVA SAFETY: Explain a movie only once. Strictly no 18+, adult, or sketch comedy movies. Family-friendly only.
    5. NO FOREIGN CHARACTERS: Strictly use English alphabets (A-Z). Translate Chinese/Korean titles to English."""
    
    user_prompt = f"Context: {context}\n\nQuestion: {question}\n\nProvide the response strictly in simple Roman Urdu/English (Minglish), without repetition, using bullet points:"
    
    data = {
        # UTILIZING A HIGH-CAPACITY ADVANCED MODEL FOR BETTER CONTEXTUAL UNDERSTANDING
        "model": "llama-3.3-70b-versatile", 
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.1 
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        
        if 'choices' not in response_data:
            return "Error: Invalid response received from the Groq API."
            
        raw_answer = response_data['choices'][0]['message']['content']
        
        # POST-PROCESSING FILTER (Double Safety Net for Vocabulary Correction)
        hindi_to_urdu = {
            "upyukt": "munasib",
            "sujhav": "suggestions",
            "aadharit": "based on",
            "vikalp": "options",
            "kahaani batati hai": "story dikhati hai",
            "starr ki hai": "is movie ki cast mein hain",
            "chunauti": "challenge",
            "sujhaunga": "tajweez karunga",
            "darshata": "dikhata",
            "kintu": "lekin",
            "yadi": "agar",
            "vichar": "khayal",
            "chunaav": "intikhab",
            "prerit": "inspire",
            "ant ": "end ",
            "parivaar": "family",
            "kathin": "mushkil",
            "paristhitiyon": "situations",
            "yuddh": "jang",
            "bhagidari": "hissa",
            "anusaar": "mutabiq"
        }
        
        final_answer = raw_answer
        for hindi, urdu in hindi_to_urdu.items():
            final_answer = final_answer.replace(hindi, urdu)
            final_answer = final_answer.replace(hindi.capitalize(), urdu.capitalize())
            
        return final_answer
        
    except Exception as e:
        return f"Execution Error: {str(e)}"