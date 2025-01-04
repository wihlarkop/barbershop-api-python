from sqlalchemy import insert, RowMapping, select
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.operators import eq

from app.entities.user import UserEntities
from app.exceptions.base_exception import InternalServerError
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
		email: str,
	) -> RowMapping:
		stmt = select(user).where(eq(user.c.email, email))

		try:
			result = await conn.execute(statement=stmt)
			return result.mappings().fetchone()
		except Exception as e:
			raise InternalServerError(message=str(e))

	async def update_user(self, conn: AsyncConnection, payload: UserEntities):
		pass
