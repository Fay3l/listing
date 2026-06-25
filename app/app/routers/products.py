
from fastapi import APIRouter

from ..schemas.products import Product


router = APIRouter(prefix="/products", tags=["products"])


@router.post("/products")
async def add_product(product: Product):
    # products.routerend(product)
    return "Ajouté"


@router.put("/products")
async def update_product(product: Product):
    # for i, p in enumerate(products):
    #     if p.id == product.id:
    #         products[i] = product
    return product


@router.delete("/products")
async def delete_product(product: Product):
    # for i, p in enumerate(products):
    #     if p.id == product.id:
    #         products.pop(i)
    return "Supprimé"
