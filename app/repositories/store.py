from typing import Sequence
from uuid import UUID

from sqlalchemy import RowMapping, and_, cast, func, select
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.operators import eq

from app.exceptions.base_exception import InternalServerError
from app.models.capster import capster
from app.models.store import store
from app.models.user import user
from app.repositories.interface import StoreInterface


class StoreRepositories(StoreInterface):
	async def get_stores(self, conn: AsyncConnection) -> Sequence[RowMapping]:
		stmt = select(
			store.c.uuid,
			store.c.store_name,
			store.c.phone_number,
			store.c.opening_hours,
			store.c.closing_hours,
		)

		try:
			result = await conn.execute(statement=stmt)
			return result.mappings().fetchall()
		except Exception as e:
			raise InternalServerError(message=str(e))

	async def get_store_by_uuid(self, store_uuid: UUID, conn: AsyncConnection) -> RowMapping | None:
		stmt = (
			select(
				store.c.uuid,
				store.c.store_name,
				store.c.address,
				store.c.phone_number,
				store.c.opening_hours,
				store.c.closing_hours,
				func.coalesce(
					func.jsonb_agg(
						func.jsonb_build_object(
							"user_uuid",
							user.c.uuid,
							"full_name",
							user.c.full_name,
						)
					).filter(and_(user.c.uuid.isnot(None)), (user.c.deleted_at.is_(None))),
					cast("[]", JSONB),
				).label("capsters"),
			)
			.join(capster, eq(store.c.uuid, capster.c.store_uuid), isouter=True)
			.join(user, eq(user.c.uuid, capster.c.user_uuid), isouter=True)
			.where(eq(store.c.uuid, store_uuid))
			.group_by(store.c.uuid)
		)

		try:
			result = await conn.execute(statement=stmt)
			return result.mappings().fetchone()
		except Exception as e:
			raise InternalServerError(message=str(e))
