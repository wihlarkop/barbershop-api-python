from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.dependency.exception import InternalServerError
from app.models.product import product


class ProductRepositories:
    async def get_products(self, conn: AsyncConnection):
        stmt = select(product)

        try:
            result = await conn.execute(statement=stmt)
            return result.fetchall()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def get_product_by_id(self, product_id: str, conn: AsyncConnection):
        stmt = select(product).filter(product.c.id == product_id)

        try:
            result = await conn.execute(statement=stmt)
            return result.scalars().one()
        except Exception as e:
            raise InternalServerError(message=str(e))
