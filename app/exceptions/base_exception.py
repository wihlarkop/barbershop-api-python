from typing import Any, Callable, Coroutine

from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from starlette.requests import Request

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
		if exc is not None and hasattr(exc, "message") and exc.message:
			error_message = exc.message

		return ORJSONResponse(
			jsonable_encoder(
				JsonResponse(
					message=error_message,
					status_code=status_code,
					data=None,
					success=False,
				)
			)
		)

	return exception_handler
