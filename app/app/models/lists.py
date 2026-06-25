from sqlalchemy import Boolean

from ..database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

class Lists(Base):
    """Products class"""
    __tablename__ = "lists"

    id: Mapped[UUID] = mapped_column(primary_key=True, init=False)
    isShared: Mapped[bool] =mapped_column(Boolean,default=False)
    products: Mapped[list['Products']] = relationship(
        default_factory=list
    )