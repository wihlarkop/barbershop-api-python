from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError

from app.helper.response import JsonResponse


async def handle_custom_http_exception(request: Request, exc: HTTPException):
    message: str = exc.detail
    status_code: int = exc.status_code

    return JsonResponse(
        message=message,
        status_code=status_code,
        data=None,
        success=False
    )


async def handle_custom_validation_error(request: Request, exc: RequestValidationError):
    return JsonResponse(
        data=f"value is {exc.body}",
        message=exc.errors(),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        success=False
    )
