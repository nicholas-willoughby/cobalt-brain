from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/call")
async def inbound_call(request: Request):
    print("Incoming call webhook")

    swml = {
        "actions": [
            {
                "say": {
                    "text": "Your FastAPI webhook is now connected."
                }
            }
        ]
    }

    return JSONResponse(content=swml)

