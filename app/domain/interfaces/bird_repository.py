from abc import ABC, abstractmethod
from app.domain.entities.bird_entity import Bird

class BirdRepository(ABC):
    @abstractmethod
    async def create(self, bird: Bird) -> Bird:
        pass
    
    @abstractmethod
    async def get_by_id(self, id: int) -> Bird | None:
        pass
    
    @abstractmethod
    async def list_birds(self) -> list[Bird]:
        pass