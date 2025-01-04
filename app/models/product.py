from datetime import datetime

from sqlalchemy import TIMESTAMP, UUID, Column, Float, String, Table, Text

from app.database.client import metadata
from app.helper.generator import timezone

product = Table(
	"product",
	metadata,
	Column(name="uuid", type_=UUID(), autoincrement=True, primary_key=True),
	Column(name="name", type_=String(), nullable=False),
	Column(name="description", type_=String(), nullable=False),
	Column(name="image", type_=Text(), nullable=False),
	Column(name="price", type_=Float(), nullable=False),
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
