from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ReviewRequest(BaseModel):
    reviews: List[str]

@app.post("/summarize-reviews/")
def summarize_reviews(request: ReviewRequest):
    if not request.reviews:
        return {"summary": "No reviews provided."}
    
    # Simple example: concatenate first two reviews as a fake summary
    summary = " ".join(request.reviews[:2])  
    return {"summary": summary}