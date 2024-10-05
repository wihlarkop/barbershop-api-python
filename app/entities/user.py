from datetime import date
from enum import StrEnum
from uuid import UUID

from app.entities.base import AuditBaseModel


class UserRoleEnum(StrEnum):
    capster = "capster"
    administrator = "administrator"
    customer = "customer"


class UserEntities(AuditBaseModel):
    uuid: UUID
    email: str
    password: str
    avatar: str | None = None
    full_name: str | None = None
    dob: date | None = None
    phone_number: str | None = None
    is_verified_customer: bool = False
    user_role: UserRoleEnum = UserRoleEnum.customer
