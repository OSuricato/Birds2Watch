# app/domain/entities/bird_entity.py needs to be created
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Bird:
    id: int | None
    name: str
    species: str
    spotted: bool = False
    created_at: datetime | None = None