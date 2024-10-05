from app.entities.base import AuditBaseModel


class ProductSchema(AuditBaseModel):
    uuid: int
    name: str
    description: str
    image: str
