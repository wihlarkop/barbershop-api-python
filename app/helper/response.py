from typing import Any

import orjson
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel


class MetaResponse(BaseModel):
    limit: int | None
    offset: int | None
    total_data: int | None = 0


class JsonResponse(ORJSONResponse):
    def __init__(
            self,
            data: Any,
            message: str,
            meta: MetaResponse = None,
            success: bool = True,
            status_code: int = 200
    ):
        self.data = data
        self.message = message
        self.success = success
        self.meta = meta
        super().__init__(content=self.render(content=data), status_code=status_code)

    def render(self, content: Any) -> bytes:
        formatted_response = {
            "data": self.data,
            "message": self.message,
            "success": self.success,
            "meta": self.meta
        }
        return orjson.dumps(
            jsonable_encoder(formatted_response), option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SERIALIZE_NUMPY
        )
