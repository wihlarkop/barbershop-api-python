"""add field store_code in table store

Revision ID: 515190466506
Revises: e148b4912b1f
Create Date: 2025-01-04 21:03:48.210240

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "515190466506"
down_revision: Union[str, None] = "e148b4912b1f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.add_column(
		table_name="store",
		column=sa.Column("store_code", sa.String(length=10), nullable=True),
	)


def downgrade() -> None:
	op.drop_column(table_name="store", column_name="store_code")
