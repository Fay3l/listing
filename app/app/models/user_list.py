from sqlalchemy import ForeignKey,Column,Table
from ..database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

users_lists_association = Table(
    "users_lists_association",
    Base.metadata,
    Column("users_id", ForeignKey("users.id"), primary_key=True),
    Column("lists_id", ForeignKey("lists.id"), primary_key=True),
)