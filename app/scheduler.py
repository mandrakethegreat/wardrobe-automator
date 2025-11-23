from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.database import SessionLocal
from app.models import User
from app.services.weather import get_weather
from app.services.llm import get_wardrobe_advice
from app.services.sms import send_sms
from sqlalchemy import select
import datetime

scheduler = AsyncIOScheduler()

async def check_and_send():
    now = datetime.datetime.now().strftime('%H:%M')
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.send_time == now, User.is_active == True))
        users = result.scalars().all()
        for user in users:
            weather = await get_weather(user.zip_code)
            advice = await get_wardrobe_advice(weather)
            await send_sms(user.phone_number, advice)

def start_scheduler():
    scheduler.add_job(check_and_send, 'interval', minutes=1)
    scheduler.start()
