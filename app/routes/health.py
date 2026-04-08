from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Your AI caller backend is running!"}
