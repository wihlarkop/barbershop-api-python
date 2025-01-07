from datetime import date
from enum import StrEnum
from uuid import UUID

from app.entities.base import AuditBaseModel


class UserRoleEnum(StrEnum):
	capster = "capster"
	administrator = "administrator"
	customer = "customer"


class UserEntities(AuditBaseModel):
	uuid: UUID | None = None
	email: str | None = None
	password: str | None = None
	avatar: str | None = None
	full_name: str | None = None
	dob: date | None = None
	phone_number: str | None = None
	is_verified_customer: bool = False
	store_code: str | None = None
	user_role: UserRoleEnum = UserRoleEnum.customer
