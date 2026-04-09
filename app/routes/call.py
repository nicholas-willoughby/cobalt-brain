from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/call")
async def inbound_call(request: Request):
    swml = {
        "actions": [
            {"say": {"text": "Your FastAPI webhook is now connected."}}
        ]
    }
    return JSONResponse(content=swml)
