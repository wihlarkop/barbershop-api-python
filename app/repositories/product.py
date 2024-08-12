from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.dependencies.exception import InternalServerError
from app.models.product import product


class ProductRepositories:
    async def get_products(self, conn: AsyncConnection):
        stmt = select(product.c.id, product.c.name, product.c.description, product.c.image)

        try:
            result = await conn.execute(statement=stmt)
            return result.mappings().fetchall()
        except Exception as e:
            raise InternalServerError(message=str(e))
