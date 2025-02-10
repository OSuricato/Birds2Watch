from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from app.domain.entities.base_entity import BaseEntity

@dataclass
class Bird(BaseEntity):

    name: str
    species: str
    spotted: bool = False
    created_at: Optional[datetime] = None

    def mark_spotted(self) -> None:
        """
        Example domain operation that marks the Bird as spotted and sets a timestamp.
        """
        self.spotted = True
        self.created_at = datetime.utcnow()