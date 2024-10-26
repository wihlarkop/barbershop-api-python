from datetime import time
from uuid import UUID

from pydantic import BaseModel


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