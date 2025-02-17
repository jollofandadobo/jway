from fastapi import APIRouter, Depends
from dependencies.dependency import get_rainforest_service
from services.openai_service import summarize_reviews

router = APIRouter()

@router.get("/{asin}")
async def get_rainforest_data(asin: str, rainforest_service=Depends(get_rainforest_service)):
    data = rainforest_service(asin)

    # Pre processing the data before it is sent to openAi API
    reviews = data["product"]["top_reviews"]
    top_reviews_body = []
    for review in reviews:
        top_reviews_body.append(review["body"])

    summary = summarize_reviews(top_reviews_body)

    return summary