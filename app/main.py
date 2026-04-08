from fastapi import FastAPI
from app.routes import health, call

app = FastAPI()

app.include_router(health.router)
app.include_router(call.router)