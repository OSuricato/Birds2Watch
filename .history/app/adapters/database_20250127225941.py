from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base

Base = declarative_base()

async def get_db_session() -> AsyncSession:
    # Implementation needed
    pass

