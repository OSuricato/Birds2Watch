from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.adapters.database import get_db_session
from app.use_cases.bird.create_bird_use_case import CreateBirdUseCase
from app.adapters.repositories.bird_repository import SQLAlchemyBirdRepository

async def get_bird_use_case(
    session: AsyncSession = Depends(get_db_session)
) -> CreateBirdUseCase:
    repository = SQLAlchemyBirdRepository(session)
    return CreateBirdUseCase(repository)