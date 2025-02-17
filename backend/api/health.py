from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "OK", "message": "API is up and running!"}
