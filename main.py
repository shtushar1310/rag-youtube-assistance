from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import ingest, chat

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    title="YouTube RAG API",
    description="Ask questions about any YouTube video using RAG",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(ingest.router, prefix="/api/v1", tags=["Ingest"])
app.include_router(chat.router,   prefix="/api/v1", tags=["Chat"])

@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "YouTube RAG API is running"}