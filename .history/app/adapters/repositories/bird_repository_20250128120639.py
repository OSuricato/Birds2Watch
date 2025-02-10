from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.entities.bird_entity import Bird
from app.domain.interfaces.bird_repository import BirdRepository
from app.adapters.persistence.models.bird_model import BirdModel

class SQLAlchemyBirdRepository(BirdRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, bird: Bird) -> Bird:
        # Convert domain entity -> ORM model
        bird_orm = BirdModel(
            name=bird.name,
            species=bird.species,
            spotted=bird.spotted
        )
        self._session.add(bird_orm)
        await self._session.commit()
        await self._session.refresh(bird_orm)

        # Convert back to domain entity
        return self._to_entity(bird_orm)

    async def get_by_id(self, bird_id: int) -> Bird | None:
        result = await self._session.execute(
            select(BirdModel).where(BirdModel.id == bird_id)
        )
        bird_orm = result.scalar_one_or_none()
        if not bird_orm:
            return None

        return self._to_entity(bird_orm)

    # ... and so on for list_birds, update, delete

    def _to_entity(self, model: BirdModel) -> Bird:
        """
        Map the ORM model to the domain entity.
        This is where we rely on knowledge of BirdModel, which belongs in the adapter layer, not the domain layer.
        """
        return Bird(
            id=model.id,
            name=model.name,
            species=model.species,
            spotted=model.spotted,
            created_at=model.created_at
        )