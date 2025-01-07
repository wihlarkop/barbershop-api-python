"""add field verification_code at table user

Revision ID: 8272ed4baf26
Revises: 515190466506
Create Date: 2025-01-08 00:24:27.142199

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '8272ed4baf26'
down_revision: Union[str, None] = '515190466506'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        table_name='user',
        column=sa.Column(
            'store_code',
            sa.String(length=10),
            nullable=True
        )
    )
    op.add_column(
        table_name='user',
        column=sa.Column(
            'verification_at',
            type_=sa.TIMESTAMP(timezone=True), nullable=True
        )
    )


def downgrade() -> None:
    op.drop_column(table_name='user', column_name='store_code')
    op.drop_column(table_name='user', column_name='verification_at')
