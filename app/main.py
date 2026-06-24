from fastapi import FastAPI
from pydantic import BaseModel
from collections.abc import AsyncIterable, Iterable
from fastapi.sse import EventSourceResponse
from uuid import uuid4

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Product(BaseModel):
    id: str
    person: str
    place: str
    id_sse: str
    product: str
    price: float
    isChecked: bool


products = []


@app.post("/create-list")
async def create_list():
    return f"{str(uuid4())}"


@app.get("/list/{list_id}/products", response_class=EventSourceResponse)
async def sse_items() -> AsyncIterable[Product]:
    for item in products:
        yield item


@app.post("/products")
async def add_product(product: Product):
    products.append(product)

@app.put("/products")
async def update_product(product: Product):
    for i, p in enumerate(products):
        if p.id == product.id:
            products[i] = product
            return product

@app.delete("/products")
async def delete_product(product: Product):
    for i, p in enumerate(products):
        if p.id == product.id:
            products.pop(i)
            return "Supprimé"