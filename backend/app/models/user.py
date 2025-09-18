from sqlalchemy import Column, Integer, String
from app.db import Base   # ✅ use database.py, not app.db

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # 🔒 will store hashed password
