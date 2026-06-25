from collections.abc import AsyncIterable
from typing import AsyncGenerator

from fastapi import APIRouter
from fastapi.sse import EventSourceResponse

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/list/{list_id}", response_class=EventSourceResponse)
async def sse_items(list_id):
    # for item in products:
    #     yield item
    yield f"{list_id}"