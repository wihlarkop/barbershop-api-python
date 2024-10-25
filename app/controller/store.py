from urllib.request import Request

from fastapi import APIRouter

from app.dependencies.database import DBConnection

store_router = APIRouter(tags=["Store"])


@store_router.get(path="", )
async def get_stores(request: Request, conn: DBConnection):
    pass


@store_router.get(path="/{store_uuid}")
async def get_store(request: Request, store_uuid: str):
    pass
