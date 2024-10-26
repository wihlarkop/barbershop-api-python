from uuid import UUID

from fastapi import APIRouter, Request, status

from app.dependencies.database import DBConnection
from app.helper.response import JsonResponse
from app.schemas.store import GetStore, GetStores
from app.services.store import StoreServices

store_router = APIRouter(tags=["Store"])


@store_router.get(path="", response_model=JsonResponse[list[GetStores]])
async def get_stores(request: Request, conn: DBConnection):
    store_services: StoreServices = request.state.store_services
    stores = await store_services.get_stores(conn=conn)
    return JsonResponse(
        data=stores,
        message="success get stores",
        status_code=status.HTTP_200_OK
    )


@store_router.get(path="/{store_uuid:uuid}", response_model=JsonResponse[GetStore])
async def get_store(request: Request, conn: DBConnection, store_uuid: UUID):
    store_services: StoreServices = request.state.store_services
    store = await store_services.get_store(conn=conn, store_uuid=store_uuid)
    return JsonResponse(
        data=store,
        message="success get store" if store else "store not found",
        status_code=status.HTTP_200_OK if store else status.HTTP_404_NOT_FOUND
    )
