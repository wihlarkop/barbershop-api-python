from typing import Sequence

from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class MetaResponse(BaseModel):
    limit: int | None
    offset: int | None
    total_data: int | None = 0


def JsonResponse(
        data: BaseModel | dict | None | list[BaseModel] | str | list[dict],
        message: str | list | Sequence | None,
        meta: dict | MetaResponse | None = None,
        success: bool = True,
        status_code: int = status.HTTP_200_OK
) -> JSONResponse:
    if meta is None:
        meta = None

    return JSONResponse(
        content={
            "data": data,
            "message": message,
            "success": success,
            "meta": meta
        },
        status_code=status_code
    )
