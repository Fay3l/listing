from typing import List

from sqlalchemy import Boolean

from ..database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from .user_list import users_lists_association


class Lists(Base):
    """Products class"""
    __tablename__ = "lists"

    id: Mapped[UUID] = mapped_column(primary_key=True, init=False)
    isShared: Mapped[bool] = mapped_column(Boolean, default=False)
    products: Mapped[list['Products']] = relationship(
        default_factory=list
    )
    users: Mapped[List[Lists]] = relationship(
        secondary=users_lists_association, back_populates="lists", default_factory=list)
