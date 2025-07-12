import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from commands import bot
from config import API_HOST, API_PORT, ARTIST_CITY_CHANNEL
import uvicorn

app = FastAPI()


class MessageRequest(BaseModel):
    userName: str
    artistName: str
    artistImage: str
    cityName: str


@app.post("/artist-city")
async def send_message(request: MessageRequest):
    await bot.send_embed(
        title="Artist City Suggestion",
        desc=f"User {request.userName} has suggested that {request.artistName} is from {request.cityName}.",
        image=request.artistImage
    )
    print(f"Send Artist City: {request}")
    return {"status": "sent"}


@app.get("/health-check")
async def send_message():
    return {"status": "ok!"}


async def serve_api():
    config = uvicorn.Config(app, host=API_HOST, port=API_PORT, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()
