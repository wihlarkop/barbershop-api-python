from uuid import UUID

from app.entities.base import AuditBaseModel


class StoreCapsterEntities(AuditBaseModel):
	uuid: UUID
	user_uuid: UUID
	store_uuid: UUID
