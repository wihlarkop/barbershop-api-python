from app.entities.base import AuditBaseModel


class ProductEntities(AuditBaseModel):
	uuid: int
	name: str
	description: str
	image: str
