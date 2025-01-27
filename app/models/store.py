from datetime import datetime

from sqlalchemy import TIMESTAMP, UUID, Column, String, Table, Text, Time

from app.database.client import metadata
from app.helper.generator import timezone

store = Table(
	"store",
	metadata,
	Column(name="uuid", type_=UUID(), primary_key=True),
	Column(name="store_name", type_=String(length=255), nullable=False),
	Column(name="address", type_=Text(), nullable=False),
	Column(name="phone_number", type_=String(length=15), nullable=False),
	Column(name="store_qr", type_=Text(), nullable=True),
	Column(name="store_code", type_=String(length=10), nullable=True),
	Column(name="opening_hours", type_=Time(), nullable=False),
	Column(name="closing_hours", type_=Time(), nullable=False),
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
)
