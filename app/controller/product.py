from fastapi import APIRouter

product_router = APIRouter(prefix="/api/v1/product", tags=["Product"])


@product_router.get(path="")
async def get_all_products():
    pass
