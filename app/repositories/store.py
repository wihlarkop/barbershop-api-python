from typing import Sequence
from uuid import UUID

from sqlalchemy import RowMapping, select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.exceptions.base_exception import InternalServerError
from app.models.store import store
from app.repositories.interface import StoreInterface


class StoreRepositories(StoreInterface):
    async def get_stores(self, conn: AsyncConnection) -> Sequence[RowMapping]:
        stmt = select(
            store.c.uuid,
            store.c.store_name,
            store.c.phone_number,
            store.c.opening_hours,
            store.c.closing_hours
        )

        try:
            result = await conn.execute(statement=stmt)
            return result.mappings().fetchall()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def get_store_by_uuid(self, store_uuid: UUID, conn: AsyncConnection) -> RowMapping | None:
        stmt = select(
            store.c.uuid,
            store.c.store_name,
            store.c.address,
            store.c.phone_number,
            store.c.opening_hours,
            store.c.closing_hours
        )

        try:
            result = await conn.execute(statement=stmt)
            return result.mappings().fetchone()
        except Exception as e:
            raise InternalServerError(message=str(e))
