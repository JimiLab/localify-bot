import asyncio

import discord
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from commands import bot
from config import API_HOST, API_PORT, ARTIST_CITY_CHANNEL
import uvicorn

app = FastAPI()


class ArtistCityRequest(BaseModel):
    userName: str
    artistName: str
    artistImage: str
    cityName: str
    isPreApproved: bool


class ModelTrainedRequest(BaseModel):
    accuracy: float
    accuracy_breakdown: list[float]
    is_worse: bool


@app.post("/artist-city")
async def artist_city(request: ArtistCityRequest):
    await bot.send_embed(
        title="Artist City Suggestion",
        desc=f"User {request.userName} has suggested that {request.artistName} is from {request.cityName}.",
        color=discord.Color.green() if request.isPreApproved else discord.Color.red(),
        image=request.artistImage,
        url="https://dash.localify.org/#/crowd-sourcing/artist/city"
    )
    print(f"Send Artist City: {request}")
    return {"status": "sent"}


@app.post("/model-trained")
async def model_trained(request: ModelTrainedRequest):
    await bot.send_embed(
        title="Model Finished Training",
        desc=f"""A model has finished training on the JimiLab server.
This model performed {'worse' if request.is_worse else 'better'} than the previous model, and the recommender system has {'not ' if request.is_worse else ''}been updated.
Accuracy: {round(request.accuracy, 4)}
Accuracy by Popularity Bucket: {list(map(lambda x: round(x, 4), request.accuracy_breakdown))}
""",
        color=discord.Color.red() if request.is_worse else discord.Color.green()
    )
    print(f"Send Model Trained: {request}")
    return {"status": "sent"}


@app.get("/health-check")
async def health_check():
    return {"status": "ok!"}


async def serve_api():
    config = uvicorn.Config(app, host=API_HOST, port=API_PORT, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()
