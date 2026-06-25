from uuid import uuid4
from fastapi import APIRouter


router = APIRouter(prefix="/products", tags=["products"])


@router.post("/")
async def create_list():
    return f"{str(uuid4())}"
