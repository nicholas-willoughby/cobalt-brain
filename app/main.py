from fastapi import FastAPI
from app.routes.call import router as call_router

app = FastAPI()

# Root route for sanity check
@app.get("/")
async def home():
    return {"status": "ok", "message": "cobalt-brain API is running"}

# Include the /call route from call.py
app.include_router(call_router)


