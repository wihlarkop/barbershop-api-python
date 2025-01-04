from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class MetaResponse(BaseModel):
	limit: int | None = None
	offset: int | None = None
	total_data: int | None = 0


class JsonResponse(BaseModel, Generic[T]):
	data: T | Any = None
	message: str = None
	success: bool = True
	meta: MetaResponse | None = None
	status_code: int = 200
