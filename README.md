# 🎬 Movies Lore Expert

Your Personal AI Cinema Guide! Movies Lore Expert is an intelligent, RAG-based AI chatbot designed to provide personalized, detailed, and highly respectful movie recommendations. It acts as a professional cinematic consultant, offering deep lore and background details for every movie.

## ✨ Features
* **Smart Recommendations:** Powered by the advanced `llama-3.3-70b-versatile` model via Groq API.
* **Viva-Safe & Family Friendly:** Strictly filters out 18+ or inappropriate content, ensuring clean and respectful suggestions.
* **Culturally Tailored:** Communicates in clear Roman Urdu/Minglish, maintaining a polite and structured bullet-point format.
* **Export Options:** Instantly download your personalized movie recommendations as a cleanly formatted PDF document.
* **Voice Search:** Integrated speech recognition for hands-free queries.

## 🛠️ Tech Stack
**Frontend:**
* HTML5, CSS3 (Dark Theme), Vanilla JavaScript
* `html2pdf.js` for exporting chat histories

**Backend:**
* Python (FastAPI / Uvicorn)
* Groq API (LLaMA-3.3-70b) for LLM inferences
* Pinecone for Vector Database & RAG Architecture

## 🚀 How to Run Locally

### 1. Backend Setup
1. Open a terminal and navigate to the `backend` directory.
2. Activate the virtual environment:
```bash
   .\venv\Scripts\activate