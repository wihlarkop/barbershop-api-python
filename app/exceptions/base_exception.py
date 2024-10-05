from typing import Callable, Any, Coroutine

from starlette.requests import Request

from app.helper.response import JsonResponse


class InternalServerError(Exception):
    def __init__(self, message: str = None):
        self.message = message
        super().__init__(self.message)


def create_exception_handler(
        status_code: int,
        message: str | None  = None
) -> Callable[[Request, Exception], Coroutine[Any, Any, JsonResponse]]:
    async def exception_handler(_: Request, exc: Exception) -> JsonResponse:
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
