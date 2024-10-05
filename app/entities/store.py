from datetime import time
from uuid import UUID

from app.entities.base import AuditBaseModel


class StoreEntities(AuditBaseModel):
    uuid: UUID
    store_name: str
    address: str
    phone_number: str
    store_qr: str
    opening_hours: time