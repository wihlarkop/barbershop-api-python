from fastapi import APIRouter, Request, status

from app.dependencies.database import DBConnection
from app.helper.response import JsonResponse
from app.schemas.customer import (
	LoginCustomerRequest,
	LoginCustomerResponse,
	RegisterCustomerRequest,
)
from app.services.customer import CustomerServices

customer_router = APIRouter(tags=["Customer"], prefix="/api/v1/customer")


@customer_router.post(path="/register")
async def register(
	request: Request, conn: DBConnection, payload: RegisterCustomerRequest
) -> JsonResponse[None]:
	customer_services: CustomerServices = request.state.customer_services
	result = await customer_services.register(payload=payload, conn=conn)
	return JsonResponse(
		data=None, message=result, status_code=status.HTTP_201_CREATED
	)


@customer_router.post(path="/login")
async def login(
	request: Request, conn: DBConnection, payload: LoginCustomerRequest
) -> JsonResponse[LoginCustomerResponse]:
	customer_services: CustomerServices = request.state.customer_services
	await customer_services.login(payload=payload, conn=conn)
	return JsonResponse(data=None, message="success login")


@customer_router.get(path="/profile")
async def profile(request: Request, conn: DBConnection) -> JsonResponse:
	pass


@customer_router.put(path="/profile")
async def update_profile(request: Request, conn: DBConnection) -> JsonResponse:
	pass


@customer_router.post(path="/activate-membership")
async def activate_membership(request: Request, conn: DBConnection) -> JsonResponse:
	pass
