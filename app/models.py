from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    zip_code = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    send_time = Column(String)  # Format HH:MM
    is_active = Column(Boolean, default=True)
