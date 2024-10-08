from fastapi import APIRouter, Request, status

from app.dependencies.database import DBConnection
from app.helper.response import JsonResponse
from app.services.product import ProductServices

product_router = APIRouter(prefix="/api/v1/product", tags=["Product"])


@product_router.get(path="")
async def get_all_products(request: Request, conn: DBConnection):
    product_services: ProductServices = request.state.product_services
    products = await product_services.get_all_products(conn=conn)
    return JsonResponse(
        data=products,
        message="success get products",
        status_code=status.HTTP_200_OK
    )
