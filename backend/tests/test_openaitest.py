from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from ..services.openai_service import summarize_reviews as summarize_reviews_service

app = FastAPI()

class ReviewRequest(BaseModel):
    reviews: List[str]

@app.post("/summarize-reviews/")
def summarize_reviews(request: ReviewRequest):
    if not request.reviews:
        return {"summary": "No reviews provided."}
    
    try:
        summary = summarize_reviews_service(request.reviews)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))