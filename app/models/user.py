from datetime import datetime

from sqlalchemy import Boolean, Date, String, Table, Column, Text, TIMESTAMP, UUID

from app.database.client import metadata
from app.helper.generator import timezone

user = Table(
    "user",
    metadata,
    Column(name="uuid", type_=UUID(), primary_key=True),
    Column(name="email", type_=String(length=255), unique=True, nullable=False),
    Column(name="password", type_=String(length=255), nullable=False),
    Column(name="avatar", type_=Text(), nullable=True),
    Column(name="full_name", type_=String(255), nullable=True),
    Column(name="dob", type_=Date(), nullable=True),
    Column(name="is_member", type_=Boolean(), default=False),
    Column(name="is_staff", type_=Boolean(), default=False),
    Column(name="created_at", type_=TIMESTAMP(timezone=True), default=datetime.now(tz=timezone)),
    Column(name="updated_at", type_=TIMESTAMP(timezone=True), onupdate=datetime.now(tz=timezone)),
    Column(name="verification_at", type_=TIMESTAMP(timezone=True), nullable=True),
    Column(name="deleted_at", type_=TIMESTAMP(timezone=True), nullable=True),
    Column(name="created_by", type_=String(length=255)),
    Column(name="updated_by", type_=String(length=255)),
    Column(name="deleted_by", type_=String(length=255)),
)
