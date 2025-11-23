from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import engine, Base, get_db
from app.models import User
from app.scheduler import start_scheduler
import contextlib

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    start_scheduler()
    yield

app = FastAPI(lifespan=lifespan)

class UserCreate(BaseModel):
    zip_code: str
    phone_number: str
    send_time: str

@app.post('/onboard')
async def onboard(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.phone_number == user.phone_number))
    existing_user = result.scalars().first()
    if existing_user:
        existing_user.zip_code = user.zip_code
        existing_user.send_time = user.send_time
        existing_user.is_active = True
    else:
        new_user = User(zip_code=user.zip_code, phone_number=user.phone_number, send_time=user.send_time)
        db.add(new_user)
    await db.commit()
    return {'message': 'User onboarded'}

@app.post('/sms-inbound')
async def sms_inbound(Body: str = '', From: str = '', db: AsyncSession = Depends(get_db)):
    if 'PEACE' in Body.upper():
        result = await db.execute(select(User).where(User.phone_number == From))
        user = result.scalars().first()
        if user:
            user.is_active = False
            await db.commit()
    return {'message': 'Received'}
