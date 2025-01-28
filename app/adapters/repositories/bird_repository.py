from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.bird_entity import Bird
from app.domain.interfaces.bird_repository import BirdRepository
from app.adapters.persistence.models.bird_model import BirdModel

class SQLAlchemyBirdRepository(BirdRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
        
    async def create(self, bird: Bird) -> Bird:
        bird_model = BirdModel(
            name=bird.name,
            species=bird.species
        )
        self._session.add(bird_model)
        await self._session.commit()
        
        return Bird(
            id=bird_model.id,
            name=bird_model.name,
            species=bird_model.species,
            spotted=bird_model.spotted,
            created_at=bird_model.created_at
        )