from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database.base import Base


class Products(Base):
    """Products class"""
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String, default="")
    place: Mapped[str] = mapped_column(String, default="")
    person: Mapped[str] = mapped_column(String, default="")
    isChecked: Mapped[str] = mapped_column(String, default="")
    price: Mapped[int] = mapped_column(default=0)
    list_id: Mapped[UUID] = mapped_column(ForeignKey("lists.id"), default=None)
