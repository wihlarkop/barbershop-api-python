from fastapi import APIRouter, Request
from sqlalchemy import select

from app.config import settings
from app.dependencies.database import DBConnection
from app.helper.response import JsonResponse
from app.schemas.health import HealthResponse, Status

health_router = APIRouter(tags=["Health"])


@health_router.get(path="/health", response_model=JsonResponse[HealthResponse])
async def health_check(request: Request, conn: DBConnection) -> JsonResponse:
    db_health = await conn.execute(select(1))
    health_result = db_health.scalar()

    status = Status(postgres=(health_result == 1))

    result = HealthResponse(
        name="Barbershop API",
        version=settings.APP_VERSION,
        status=status
    )

    return JsonResponse(
        data=result,
        message="OK",
    )
