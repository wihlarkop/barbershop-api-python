from app.repositories.product import ProductRepositories


class ProductServices:
    def __init__(self, product_repo: ProductRepositories):
        self.__product_repo = product_repo

    async def get_all_products(self):
        pass
