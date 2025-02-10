from dataclasses import dataclass
from datetime import datetime

@dataclass
class Bird(BaseEntity):
    id: int | None
    name: str
    species: str
    spotted: bool = False
    created_at: datetime | None = None