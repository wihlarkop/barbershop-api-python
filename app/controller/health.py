from fastapi import APIRouter, Request
from sqlalchemy import select

from app.config import settings
from app.dependencies.database import DBConnection
from app.helper.response import JsonResponse

health_router = APIRouter(tags=["Health"])


@health_router.get(path="/health")
async def health_check(request: Request, conn: DBConnection) -> JsonResponse:
    result = {
        "name": "Barbershop API",
        "version": settings.APP_VERSION,
        "status": {}
    }

    db_health = await conn.execute(select(1))
    health_result = db_health.scalar()

    if health_result == 1:
        result["status"] = {"postgres": True}

    return JsonResponse(
        data=result,
        message="OK",
    )
