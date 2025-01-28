from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)  # echo=True for debug logs
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)