from pydantic import BaseModel


class Product(BaseModel):
    id: str
    person: str
    place: str
    id_sse: str
    product: str
    price: float
    isChecked: bool