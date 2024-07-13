from fastapi import APIRouter, Request, status

from app.dependency.database import DBConnection
from app.helper.response import JsonResponse
from app.schemas.customer import LoginCustomer, RegisterCustomer
from app.services.customer import CustomerServices

customer_router = APIRouter(prefix="/api/v1/customer", tags=["Customer"])


@customer_router.post(path="/register")
async def register(request: Request, conn: DBConnection, payload: RegisterCustomer) -> JsonResponse:
    customer_services: CustomerServices = request.state.customer_services
    await customer_services.register(payload=payload, conn=conn)
    return JsonResponse(data=None, message="success register", status_code=status.HTTP_201_CREATED)


@customer_router.post(path="/login")
async def login(request: Request, conn: DBConnection, payload: LoginCustomer) -> JsonResponse:
    customer_services: CustomerServices = request.state.customer_services
    await customer_services.login(payload=payload, conn=conn)
    return JsonResponse(data=None, message="success login")
