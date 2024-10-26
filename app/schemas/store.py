from datetime import time
from uuid import UUID

from pydantic import BaseModel


class GetStoreCapster(BaseModel):
    user_uuid: UUID | None = None
    full_name: str | None = None

class GetStores(BaseModel):
    uuid: UUID
    store_name: str
    phone_number: str
    opening_hours: time
    closing_hours: time


class GetStore(BaseModel):
    uuid: UUID
    store_name: str
    address: str
    phone_number: str
    opening_hours: time
    closing_hours: time
    capsters: list[GetStoreCapster] | list = []