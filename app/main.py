from fastapi import FastAPI
from app.routes.call import router as call_router

app = FastAPI()

# Mount the call router so /call GET and POST actually exist
app.include_router(call_router)

@app.get("/")
async def root():
    return {"status": "ok"}



