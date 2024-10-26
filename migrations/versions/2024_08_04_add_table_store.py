"""add table store

Revision ID: eb5d4d44f19b
Revises: 69dca0431dfc
Create Date: 2024-08-04 21:50:55.100287

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from app.helper.generator import timezone

# revision identifiers, used by Alembic.
revision: str = 'eb5d4d44f19b'
down_revision: Union[str, None] = '69dca0431dfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "store",
        sa.Column(name="uuid", type_=sa.UUID(), primary_key=True),
        sa.Column(name="store_name", type_=sa.String(length=255), nullable=False),
        sa.Column(name="address", type_=sa.Text(), nullable=False),
        sa.Column(name="phone_number", type_=sa.String(length=15), nullable=False),
        sa.Column(name="store_qr", type_=sa.Text(), nullable=True),
        sa.Column(name="opening_hours", type_=sa.Time(), nullable=False),
        sa.Column(name="closing_hours", type_=sa.Time(), nullable=False),
        sa.Column(name="created_at", type_=sa.TIMESTAMP(timezone=True), default=datetime.now(tz=timezone)),
        sa.Column(name="updated_at", type_=sa.TIMESTAMP(timezone=True), onupdate=datetime.now(tz=timezone)),
        sa.Column(name="deleted_at", type_=sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column(name="created_by", type_=sa.String(length=255)),
        sa.Column(name="updated_by", type_=sa.String(length=255)),
        sa.Column(name="deleted_by", type_=sa.String(length=255)),
    )


def downgrade() -> None:
    op.drop_table(table_name="store")
    # op.drop_constraint(constraint_name="valid_phone_number", table_name="store")
