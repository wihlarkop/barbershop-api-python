from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import eq

from app.models.user import user
from app.schemas.user import UserSchema


class UserRepositories:

    async def create_user(self, payload: UserSchema, session: AsyncSession):
        pass

    async def get_user(self, email: str, session: AsyncSession):
        stmt = select(user).where(eq(user.c.email, email))

        try:
            result = await session.execute(statement=stmt)
            return result.scalar()
        except Exception:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="failed to get data")
