from pydantic import BaseModel
from datetime import datetime
from app.domain.entities.bird_entity import Bird

class BirdCreate(BaseModel):
    name: str
    species: str

class BirdResponse(BaseModel):
    id: int
    name: str
    species: str
    spotted: bool
    created_at: datetime

    @classmethod
    def from_entity(cls, bird: Bird) -> "BirdResponse":
        return cls(
            id=bird.id,
            name=bird.name,
            species=bird.species,
            spotted=bird.spotted,
            created_at=bird.created_at
        )