from uuid import UUID

from fastapi import APIRouter, Request, status

from app.dependencies.database import DBConnection
from app.helper.response import JsonResponse
from app.schemas.product import GetProducts
from app.services.product import ProductServices

product_router = APIRouter(tags=["Product"])


@product_router.get(path="", response_model=JsonResponse[list[GetProducts]])
async def get_all_products(request: Request, conn: DBConnection):
	product_services: ProductServices = request.state.product_services
	products = await product_services.get_all_products(conn=conn)
	return JsonResponse(
		data=products,
		message="success get products",
		status_code=status.HTTP_200_OK
	)


@product_router.get(path="/{product_uuid:uuid}")
async def get_product(request: Request, conn: DBConnection, product_uuid: UUID):
	pass
