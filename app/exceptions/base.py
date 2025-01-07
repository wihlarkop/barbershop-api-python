from typing import Any, Callable, Coroutine

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import ORJSONResponse
from starlette.requests import Request

from app.exceptions.token import TokenExpired, TokenInvalid
from app.exceptions.user import UserAlreadyExists, UserNotFound
from app.helper.response import JsonResponse


class InternalServerError(Exception):
    def __init__(self, message: str = None):
        self.message = message
        super().__init__(self.message)


def create_exception_handler(
    status_code: int,
    message: str | None = None
) -> Callable[[Request, Exception], Coroutine[Any, Any, ORJSONResponse]]:
    async def exception_handler(_: Request, exc: Exception) -> ORJSONResponse:
        error_message = message
        code = status_code
        if isinstance(exc, HTTPException):
            error_message = exc.detail
            code = exc.status_code

        if exc is not None and hasattr(exc, "message") and exc.message:
            error_message = exc.message
        return ORJSONResponse(
            jsonable_encoder(
                JsonResponse(
                    message=error_message,
                    status_code=code,
                    data=None,
                    success=False,
                )
            )
        )

    return exception_handler


exception_handlers = {
    HTTPException: create_exception_handler(
        status_code=status.HTTP_400_BAD_REQUEST, message="Something Wrong"
    ),
    ResponseValidationError: create_exception_handler(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR),
    InternalServerError: create_exception_handler(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message="something went wrong",
    ),
    UserAlreadyExists: create_exception_handler(status_code=status.HTTP_409_CONFLICT),
    UserNotFound: create_exception_handler(status_code=status.HTTP_404_NOT_FOUND),
    TokenExpired: create_exception_handler(
        status_code=status.HTTP_401_UNAUTHORIZED,
        message="Refresh token expired, login required.",
    ),
    TokenInvalid: create_exception_handler(
        status_code=status.HTTP_403_FORBIDDEN, message="Invalid refresh token."
    ),
}
