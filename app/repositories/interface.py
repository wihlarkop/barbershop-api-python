from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncConnection

from app.entities.user import UserSchema


class UserInterface(Protocol):
    async def create_user(self, payload: UserSchema, conn: AsyncConnection) -> None: ...

    async def get_user(self, email: str, conn: AsyncConnection): ...


class ProductInterface(Protocol):
    async def get_products(self, conn: AsyncConnection): ...
