from typing import Any, Generic, TypeVar

from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from orjson import orjson
from pydantic import BaseModel

from app.dependencies.database import DBConnection
from app.helper.response import JsonResponse
from app.schemas.customer import LoginCustomerRequest, RegisterCustomerRequest
from app.services.customer import CustomerServices

customer_router = APIRouter(tags=["Customer"])


@customer_router.post(path="/register")
async def register(request: Request, conn: DBConnection, payload: RegisterCustomerRequest) -> JsonResponse:
    customer_services: CustomerServices = request.state.customer_services
    result = await customer_services.register(payload=payload, conn=conn)
    return JsonResponse(data=result, message="success register", status_code=status.HTTP_201_CREATED)


@customer_router.post(path="/login")
async def login(request: Request, conn: DBConnection, payload: LoginCustomerRequest) -> JsonResponse:
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
