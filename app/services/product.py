from sqlalchemy.ext.asyncio import AsyncConnection

from app.repositories.interface import ProductInterface
from app.schemas.product import GetProducts


class ProductServices:
    def __init__(self, product_repo: ProductInterface):
        self.__product_repo = product_repo

    async def get_all_products(self, conn: AsyncConnection) -> list[GetProducts]:
        products = await self.__product_repo.get_products(conn=conn)
        results: list[GetProducts] = [GetProducts.model_validate(product) for product in products]
        return results
