from typing import Protocol, Sequence
from uuid import UUID

from sqlalchemy import RowMapping
from sqlalchemy.ext.asyncio import AsyncConnection

from app.entities.user import UserEntities


class UserInterface(Protocol):
    async def create_user(self, payload: UserEntities, conn: AsyncConnection): ...

    async def get_user_by_email(self, email: str, conn: AsyncConnection): ...

    async def update_user(self): ...

    async def activate_user(self): ...


class ProductInterface(Protocol):
    async def get_products(self, conn: AsyncConnection) -> Sequence[RowMapping]: ...

    async def get_product_by_uuid(self, product_uuid: UUID): ...


class StoreInterface(Protocol):
    async def get_stores(self, conn: AsyncConnection): ...

    async def get_store_by_uuid(self, store_uuid: UUID): ...


class TransactionInterface(Protocol):
    async def get_histories_by_email(self, conn: AsyncConnection): ...

    async def get_history_by_uuid(self, history_uuid: UUID): ...
