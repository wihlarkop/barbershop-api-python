"""add table user

Revision ID: 73571cb9fb09
Revises:
Create Date: 2024-07-14 02:16:28.150807

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from app.helper.generator import timezone

# revision identifiers, used by Alembic.
revision: str = "73571cb9fb09"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.create_table(
		"user",
		sa.Column(name="uuid", type_=sa.UUID(), primary_key=True),
		sa.Column(name="email", type_=sa.String(length=255), unique=True, nullable=False),
		sa.Column(name="password", type_=sa.String(length=255), nullable=False),
		sa.Column(name="avatar", type_=sa.Text, nullable=True),
		sa.Column(name="full_name", type_=sa.String(255), nullable=True),
		sa.Column(name="dob", type_=sa.Date(), nullable=True),
		sa.Column(name="phone_number", type_=sa.String(length=15)),
		sa.Column(name="is_verified_customer", type_=sa.Boolean(), default=False),
		sa.Column(
			name="user_role_enum",
			type_=sa.Enum("capster", "administrator", "customer", name="user_role_enum"),
			default="customer",
			nullable=False,
		),
		sa.Column(
			name="created_at",
			type_=sa.TIMESTAMP(timezone=True),
			default=datetime.now(tz=timezone),
		),
		sa.Column(
			name="updated_at",
			type_=sa.TIMESTAMP(timezone=True),
			onupdate=datetime.now(tz=timezone),
		),
		sa.Column(name="deleted_at", type_=sa.TIMESTAMP(timezone=True), nullable=True),
		sa.Column(name="created_by", type_=sa.String(length=255)),
		sa.Column(name="updated_by", type_=sa.String(length=255)),
		sa.Column(name="deleted_by", type_=sa.String(length=255)),
	)


def downgrade() -> None:
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table(table_name="user")
	user_role_enum = sa.Enum(name="user_role_enum")
	user_role_enum.drop(op.get_bind())
	# ### end Alembic commands ###
