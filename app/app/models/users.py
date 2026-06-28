""" Table User """
import datetime

from .lists import Lists
from ..database.base import Base
# pyright: ignore[reportMissingImports]
from sqlalchemy import DateTime, String
# pyright: ignore[reportMissingImports]
# pyright: ignore[reportMissingImports]
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func  # pyright: ignore[reportMissingImports]
from uuid import UUID, uuid4  # pyright: ignore[reportMissingImports]
from datetime import datetime, timezone
from .user_list import users_lists_association
from typing import List


class Users(Base):
    """ User """
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, init=False)
    email: Mapped[str] = mapped_column(String, default="")
    password_hash: Mapped[str] = mapped_column(String, default="")
    name: Mapped[str] = mapped_column(String, default="")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
    lists: Mapped[List[Lists]] = relationship(
        secondary=users_lists_association, back_populates="users",default_factory=list
    )