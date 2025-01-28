from app.domain.entities.bird_entity import Bird
from app.domain.interfaces.bird_repository import BirdRepository

class CreateBirdUseCase:
    def __init__(self, bird_repository: BirdRepository):
        self._repository = bird_repository
        
    async def execute(self, name: str, species: str) -> Bird:
        bird = Bird(
            id=None,
            name=name,
            species=species
        )
        return await self._repository.create(bird)