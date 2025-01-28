# app/adapters/persistence/models/bird_model.py
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func
from app.adapters.database import Base

class BirdModel(Base):
    __tablename__ = "birds"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    spotted = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())