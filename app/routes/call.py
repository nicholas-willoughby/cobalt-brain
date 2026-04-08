from fastapi import APIRouter

router = APIRouter(prefix="/call")

@router.post("/")
def start_call(phone_number: str):
    return {
        "status": "initiated",
        "phone_number": phone_number,
        "message": "Call request received. AI caller will dial shortly."
    }
