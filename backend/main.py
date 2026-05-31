from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import ChatRequest, ChatResponse
from services.embedding_service import get_embedding
from services.pinecone_service import query_pinecone
from services.llm_service import get_llm_response

app = FastAPI()

# Allow the frontend to connect.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    vector = get_embedding(request.question)
    context = query_pinecone(vector)
    print("\n=== PINECONE SE AANE WALA DATA ===")
    print(context)
    print("==================================\n")
    answer = get_llm_response(request.question, context)
    return {"answer": answer}