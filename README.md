# 🎬 Movies Lore Expert - Your Ultimate AI Cinema Oracle

Welcome to **Movies Lore Expert**, an advanced Full-Stack AI-powered chatbot that goes far beyond basic movie recommendations. It acts as your personal cinema historian and deep-dive cinematic companion, designed to uncover the hidden depths of the film universe.

## 🚀 Beyond Recommendations: The Core Capabilities
While the system excels at suggesting the perfect movie based on context and mood, its true power lies in **Deep Lore Extraction**. You can ask the AI anything, and it will deliver:

* 🕵️ **Hidden Details & Easter Eggs:** Uncover obscure facts, director's secrets, and behind-the-scenes trivia that you won't find in a standard synopsis.
* 🎭 **In-Depth Character Analysis:** Dive deeply into character motivations, hidden backstories, psychological breakdowns, and character arcs across different movies.
* 🧠 **Thematic & Plot Deconstruction:** Ask the AI to explain complex endings, hidden meanings, and philosophical themes within specific films.
* 🍿 **Smart Semantic Recommendations:** Powered by a rich dataset of **5,000 movies**, the AI understands conversational queries to suggest films based on highly specific moods, tropes, or blended genres.

## ⚙️ How It Works
Instead of relying on simple keyword matching, Movies Lore Expert utilizes advanced **Natural Language Processing (NLP)** and **Vector Embeddings**. It converts your natural language prompts into mathematical vectors to perform a highly accurate semantic search across its vast cinematic database, feeding the retrieved context to a cutting-edge LLM for a conversational response.

## 🛠️ Technical Architecture
* **Frontend:** Interactive, dark-themed UI deployed on **Vercel**.
* **Backend:** Robust API built with **Python (FastAPI)**, deployed on **Render**.
* **Vector Database:** **Pinecone** (for lightning-fast similarity and semantic search).
* **AI Embeddings:** **Hugging Face** (`all-MiniLM-L6-v2` pipeline for precise feature extraction).
* **LLM Integration:** **Groq API** (for generating detailed, engaging, and human-like cinematic lore responses).