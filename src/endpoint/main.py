from fastapi import FastAPI

api = FastAPI()

@api.get("/")
async def healthy():
    return {"200": "Healthy"}