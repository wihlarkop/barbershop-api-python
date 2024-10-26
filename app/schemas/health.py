from pydantic import BaseModel


class Status(BaseModel):
    postgres: bool | None = None


class HealthResponse(BaseModel):
    name: str
    version: str
    status: Status
