import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://localhost:5432/birds_2_watch_db")
    # Add other config parameters as needed

settings = Settings()