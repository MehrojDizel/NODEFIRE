from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr
import httpx
import os
from datetime import datetime

app = FastAPI()

# ── Telegram config (через .env или переменные окружения) ──
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")


class Lead(BaseModel):
    name: str
    phone: str
    email: str
    gpu: str
    message: str = ""


async def send_telegram(lead: Lead):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️  Telegram не настроен — пропускаем уведомление")
        return

    text = (
        f"🔥 *Новая заявка — NODEFIRE*\n\n"
        f"👤 *Имя:* {lead.name}\n"
        f"📞 *Телефон:* {lead.phone}\n"
        f"✉️ *Email:* {lead.email}\n"
        f"🖥 *GPU:* {lead.gpu}\n"
        f"💬 *Задача:* {lead.message or '—'}\n\n"
        f"🕐 {datetime.now().strftime('%d.%m.%Y %H:%M')}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        })
        if resp.status_code != 200:
            print(f"Telegram error: {resp.text}")


@app.post("/api/lead")
async def create_lead(lead: Lead):
    # Здесь можно добавить сохранение в БД
    print(f"[LEAD] {lead.name} | {lead.phone} | {lead.gpu}")
    await send_telegram(lead)
    return {"status": "ok", "message": "Заявка принята"}


# Отдаём фронт — должен быть последним
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
