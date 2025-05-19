# api.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
from telethon import TelegramClient

app = FastAPI()

api_id = int(os.getenv("API_ID", "123456"))  # Подставь свои значения или используй ENV
api_hash = os.getenv("API_HASH", "your_api_hash")
client = TelegramClient("session", api_id, api_hash)


class MessageRequest(BaseModel):
    chat_id: str
    message: str

@app.on_event("startup")
async def startup_event():
    await client.start()

@app.post("/send_message")
async def send_message(req: MessageRequest):
    await client.send_message(req.chat_id, req.message)
    return {"status": "sent"}
