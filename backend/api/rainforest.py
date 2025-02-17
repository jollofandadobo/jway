from fastapi import APIRouter, Depends
from dependencies.dependency import get_rainforest_service

router = APIRouter()

@router.get("/{asin}")
async def get_rainforest_data(asin: str, rainforest_service=Depends(get_rainforest_service)):
    return rainforest_service(asin)