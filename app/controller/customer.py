
from fastapi import APIRouter, Request

from app.dependency.database import DBSession
from app.helper.response import JsonResponse
from app.schemas.customer import RegisterCustomer
from app.services.customer import CustomerServices

customer_router = APIRouter(prefix="/api/v1/customer", tags=["Customer"])


@customer_router.post(path="/register")
async def register(request: Request, session: DBSession, payload: RegisterCustomer) -> JsonResponse:
    customer_services: CustomerServices = request.state.customer_services
    await customer_services.register(payload=payload, session=session)
    return JsonResponse(data=None, message="success register")


@customer_router.post(path="/login")
async def login(request: Request, session: DBSession) -> JsonResponse:
    pass
