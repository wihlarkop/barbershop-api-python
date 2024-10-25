from fastapi import APIRouter, Request

from app.dependencies.database import DBConnection

transaction_router = APIRouter(tags=["Transaction"])


@transaction_router.get(path="", )
async def get_transactions(request: Request, conn: DBConnection):
    pass


@transaction_router.get(path="/{transaction_uuid}")
async def get_transaction(request: Request, transaction_uuid):
    pass
