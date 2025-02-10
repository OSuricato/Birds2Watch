# app/domain/entities/base_entity.py
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class BaseEntity:
    """
    A minimal base class for all domain entities.
    This class should avoid references to infrastructure (ORM, DB sessions, etc.).
    Only place truly universal fields and methods here.
    """
    id: Optional[int] = None