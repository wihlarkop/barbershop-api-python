from uuid import UUID

from pydantic import BaseModel


class GetProducts(BaseModel):
    uuid: UUID
    name: str
    description: str
    image: str
