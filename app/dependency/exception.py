from typing import Callable

from fastapi import Request
from starlette.responses import JSONResponse

from app.helper.response import JsonResponse


class InternalServerError(Exception):
    def __init__(self, message: str = None):
        self.message = message
        super().__init__(self.message)


def create_exception_handler(
        status_code: int, message: str
) -> Callable[[Request, Exception], JsonResponse]:
    async def exception_handler(_: Request, exc: Exception) -> JSONResponse:
        error_message = message
        if exc is not None and hasattr(exc, 'message') and exc.message:
            error_message = exc.message

        return JsonResponse(
            message=error_message,
            status_code=status_code,
            data=None,
            success=False
        )

    return exception_handler
