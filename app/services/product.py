from sqlalchemy.ext.asyncio import AsyncConnection

from app.repositories.interface import ProductInterface
from app.schemas.product import GetProducts


class ProductServices:
    def __init__(self, product_repo: ProductInterface):
        self.__product_repo = product_repo

    async def get_all_products(self, conn: AsyncConnection) -> list[GetProducts]:
        results: list[GetProducts] = []
        products = await self.__product_repo.get_products(conn=conn)
        for product in products:
            results.append(GetProducts.model_validate(product))
        return results
