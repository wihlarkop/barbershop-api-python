from pydantic import EmailStr
from sqlalchemy import RowMapping, insert, select, update
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.operators import eq

from app.entities.user import UserEntities
from app.exceptions.base import InternalServerError
from app.helper.generator import generate_time_now
from app.models.user import user
from app.repositories.interface import UserInterface


class UserRepositories(UserInterface):
    async def create_user(self, conn: AsyncConnection, payload: UserEntities) -> None:
        stmt = insert(user).values(**payload.model_dump(exclude_unset=True))

        try:
            await conn.execute(statement=stmt)
            await conn.commit()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def get_user_by_email(
        self,
        conn: AsyncConnection,
        email: EmailStr,
    ) -> RowMapping:
        stmt = select(user).where(eq(user.c.email, email))

        try:
            result = await conn.execute(statement=stmt)
            return result.mappings().fetchone()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def update_user(self, conn: AsyncConnection, payload: UserEntities):
        stmt = update(user).where(eq(user.c.email, payload.email)).values(**payload.model_dump(exclude_unset=True))

        try:
            await conn.execute(statement=stmt)
            await conn.commit()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def activate_user(self, conn: AsyncConnection, payload: UserEntities):
        stmt = update(
            user
        ).where(
            eq(user.c.email, payload.email)
        ).values(
            is_verified_customer=True,
            verification_at=generate_time_now(),
            store_code=payload.store_code,
        )

        try:
            await conn.execute(statement=stmt)
            await conn.commit()
        except Exception as e:
            raise InternalServerError(message=str(e))

