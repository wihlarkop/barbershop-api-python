from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.helper.database import engine


async def get_session() -> AsyncSession:
    session = async_sessionmaker(bind=engine, class_=AsyncSession)
    async with session() as session:
        yield session
        await session.commit()


DBSession = Annotated[AsyncSession, Depends(get_session)]
