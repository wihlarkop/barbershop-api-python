from typing import Protocol, Sequence
from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import RowMapping
from sqlalchemy.ext.asyncio import AsyncConnection

from app.entities.user import UserEntities


class UserInterface(Protocol):
    async def create_user(self, conn: AsyncConnection, payload: UserEntities): ...

    async def get_user_by_email(self, conn: AsyncConnection, email: EmailStr): ...

    async def update_user(self, conn: AsyncConnection, payload: UserEntities): ...

    async def activate_user(self, conn: AsyncConnection, payload: UserEntities): ...


class ProductInterface(Protocol):
    async def get_products(self, conn: AsyncConnection) -> Sequence[RowMapping]: ...

    async def get_product_by_uuid(self, conn: AsyncConnection, product_uuid: UUID): ...


class StoreInterface(Protocol):
    async def get_stores(self, conn: AsyncConnection) -> Sequence[RowMapping]: ...

    async def get_store_by_uuid(
        self, store_uuid: UUID, conn: AsyncConnection
    ) -> RowMapping | None: ...

    async def get_store_by_store_code(self, conn: AsyncConnection, store_code: str): ...


class TransactionInterface(Protocol):
    async def get_histories_by_email(self, conn: AsyncConnection): ...

    async def get_history_by_uuid(self, history_uuid: UUID, conn: AsyncConnection): ...
