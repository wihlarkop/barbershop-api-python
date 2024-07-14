from sqlalchemy.ext.asyncio import AsyncConnection

from app.repositories.product import ProductRepositories
from app.schemas.product import GetProducts


class ProductServices:
    def __init__(self, product_repo: ProductRepositories):
        self.__product_repo = product_repo

    async def get_all_products(self, conn: AsyncConnection) -> list[GetProducts]:
        results: list[GetProducts] = []
        products = await self.__product_repo.get_products(conn=conn)
        for product in products:
            results.append(
                GetProducts(
                    id=product.id,
                    name=product.name,
                    description=product.description,
                    image=product.image,
                )
            )
        return results
