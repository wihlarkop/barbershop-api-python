from typing import Sequence

from sqlalchemy import select, RowMapping
from sqlalchemy.ext.asyncio import AsyncConnection

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
