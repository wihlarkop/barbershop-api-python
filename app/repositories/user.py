from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.operators import eq

from app.exceptions.base_exception import InternalServerError
from app.models.user import user
from app.repositories.interface import UserInterface
from app.entities.user import UserSchema


class UserRepositories(UserInterface):

    async def create_user(self, payload: UserSchema, conn: AsyncConnection) -> None:
        stmt = insert(user).values(**payload.model_dump(exclude_unset=True))

        try:
            await conn.execute(statement=stmt)
            await conn.commit()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def get_user(self, email: str, conn: AsyncConnection):
        stmt = select(user).where(eq(user.c.email, email))

        try:
            result = await conn.execute(statement=stmt)
            return result.fetchone()
        except Exception as e:
            raise InternalServerError(message=str(e))
