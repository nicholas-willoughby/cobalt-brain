from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()

@router.post("/call")
async def handle_call():
    xml = """
    <Response>
        <Say>Your FastAPI webhook is now connected.</Say>
    </Response>
    """
    return Response(content=xml, media_type="application/xml")


