# app/domain/entities/base_entity.py
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class BaseEntity:
    id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.now())
    updated_at: Optional[datetime] = None

    def mark_updated(self):
        """Update the `updated_at` timestamp. Could be used in domain logic."""
        self.updated_at = datetime.now()