from datetime import datetime

from sqlalchemy import TIMESTAMP, UUID, Column, ForeignKeyConstraint, String, Table

from app.database.client import metadata
from app.helper.generator import timezone

capster = Table(
	"capster",
	metadata,
	Column(name="uuid", type_=UUID(), primary_key=True),
	Column(name="user_uuid", type_=UUID()),
	Column(name="store_uuid", type_=UUID()),
	Column(
		name="created_at",
		type_=TIMESTAMP(timezone=True),
		default=datetime.now(tz=timezone),
	),
	Column(
		name="updated_at",
		type_=TIMESTAMP(timezone=True),
		onupdate=datetime.now(tz=timezone),
	),
	Column(name="deleted_at", type_=TIMESTAMP(timezone=True), nullable=True),
	Column(name="created_by", type_=String(length=255)),
	Column(name="updated_by", type_=String(length=255)),
	Column(name="deleted_by", type_=String(length=255)),
	ForeignKeyConstraint(
		name="fk_store_capster_user", columns=["user_uuid"], refcolumns=["user.uuid"]
	),
	ForeignKeyConstraint(
		name="fk_store_capster_store", columns=["store_uuid"], refcolumns=["store.uuid"]
	),
)
