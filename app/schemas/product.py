from pydantic import BaseModel

from app.schemas.base import AuditBaseModel


class ProductSchema(AuditBaseModel):
    id: int
    name: str
    description: str
    image: str


class GetProducts(BaseModel):
    id: int
    name: str
    description: str
    image: str
