from datetime import date
from uuid import UUID

from app.entities.base import AuditBaseModel


class UserSchema(AuditBaseModel):
    uuid: UUID
    email: str
    password: str
    avatar: str | None = None
    full_name: str | None = None
    dob: date | None = None
    is_member: bool = False
    is_staff: bool = False
