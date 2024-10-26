from datetime import datetime

from sqlalchemy import Column, ForeignKeyConstraint, Table, TIMESTAMP, UUID

from app.database.client import metadata
from app.helper.generator import timezone

verification = Table(
    "verification",
    metadata,
    Column(name="uuid", type_=UUID(), primary_key=True),
    Column(name="user_uuid", type_=UUID(), nullable=False),
    Column(name="store_uuid", type_=UUID(), nullable=False),
    Column(name="verification_at", type_=TIMESTAMP(timezone=True), default=datetime.now(tz=timezone)),

    ForeignKeyConstraint(name="fk_verification_user", columns=["user_uuid"], refcolumns=["user.uuid"]),
    ForeignKeyConstraint(name="fk_verification_store", columns=["store_uuid"], refcolumns=["store.uuid"]),
)
