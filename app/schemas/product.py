from pydantic import BaseModel


class GetProducts(BaseModel):
    uuid: int
    name: str
    description: str
    image: str
