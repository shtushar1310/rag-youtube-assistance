from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from ingest import ingest as ingest_video

router = APIRouter()

class IngestRequest(BaseModel):
    youtube_url: str

class IngestResponse(BaseModel):
    message: str
    youtube_url: str
    chunks_stored: int

@router.post("/ingest", response_model=IngestResponse)
def ingest_endpoint(body: IngestRequest):
    try:
        chunks_count = ingest_video(body.youtube_url)  # see updated ingest.py below
        return IngestResponse(
            message="Video ingested successfully",
            youtube_url=body.youtube_url,
            chunks_stored=chunks_count
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))