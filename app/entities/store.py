from datetime import time
from uuid import UUID

from app.entities.base import AuditBaseModel


class StoreEntities(AuditBaseModel):
	uuid: UUID
	store_name: str
	address: str | None = None
	phone_number: str | None = None
	store_qr: str | None = None
	opening_hours: time | None = None
	closing_hours: time | None = None
