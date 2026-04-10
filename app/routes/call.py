from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()

@router.get("/call")
async def handle_call_get():
    xml = """
    <Response>
        <Say>Your FastAPI webhook is now connected.</Say>
    </Response>
    """
    return Response(content=xml, media_type="application/xml")

@router.post("/call")
async def handle_call_post():
    xml = """
    <Response>
        <Say>Your FastAPI webhook is now connected.</Say>
    </Response>
    """
    return Response(content=xml, media_type="application/xml")


