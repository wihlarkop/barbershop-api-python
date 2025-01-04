"""add table verification

Revision ID: e148b4912b1f
Revises: 8cf239a8826f
Create Date: 2024-10-27 02:07:17.614013

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from app.helper.generator import timezone

# revision identifiers, used by Alembic.
revision: str = "e148b4912b1f"
down_revision: Union[str, None] = "8cf239a8826f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.create_table(
		"verification",
		sa.Column(name="uuid", type_=sa.UUID(), primary_key=True),
		sa.Column(name="user_uuid", type_=sa.UUID()),
		sa.Column(name="store_uuid", type_=sa.UUID()),
		sa.Column(
			name="verification_at",
			type_=sa.TIMESTAMP(timezone=True),
			default=datetime.now(tz=timezone),
		),
		sa.ForeignKeyConstraint(
			name="fk_verification_user", columns=["user_uuid"], refcolumns=["user.uuid"]
		),
		sa.ForeignKeyConstraint(
			name="fk_verification_store",
			columns=["store_uuid"],
			refcolumns=["store.uuid"],
		),
	)


def downgrade() -> None:
	op.drop_table(table_name="verification")
