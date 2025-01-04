from typing import Sequence
from uuid import UUID

from sqlalchemy import RowMapping, select
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.operators import eq

from app.exceptions.base_exception import InternalServerError
from app.models.product import product
from app.repositories.interface import ProductInterface


class ProductRepositories(ProductInterface):
	async def get_products(self, conn: AsyncConnection) -> Sequence[RowMapping]:
		stmt = select(product.c.uuid, product.c.name, product.c.description, product.c.image)

		try:
			result = await conn.execute(statement=stmt)
			return result.mappings().fetchall()
		except Exception as e:
			raise InternalServerError(message=str(e))

	async def get_product_by_uuid(self, conn: AsyncConnection, product_uuid: UUID) -> RowMapping:
		stmt = select(
			product.c.uuid,
			product.c.name,
			product.c.description,
			product.c.image,
			product.c.price,
		).where(eq(product.c.uuid, product_uuid))

		try:
			result = await conn.execute(statement=stmt)
			return result.mappings().fetchone()
		except Exception as e:
			raise InternalServerError(message=str(e))
