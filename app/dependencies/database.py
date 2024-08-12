from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncConnection

from app.database.client import engine


async def get_connection() -> AsyncConnection:
    async with engine.connect() as connection:
        yield connection


DBConnection = Annotated[AsyncConnection, Depends(get_connection)]
