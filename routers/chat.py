from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from rag_chain import build_chain

router = APIRouter()

# Build chain once at module load — avoids rebuilding on every request
chain = build_chain()

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    question: str
    answer: str

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(body: ChatRequest):
    try:
        answer = chain.invoke(body.question)
        return ChatResponse(question=body.question, answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))