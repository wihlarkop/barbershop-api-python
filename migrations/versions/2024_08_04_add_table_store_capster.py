"""add table store capster

Revision ID: 94992a42f35b
Revises: eb5d4d44f19b
Create Date: 2024-08-04 22:12:32.450614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94992a42f35b'
down_revision: Union[str, None] = 'eb5d4d44f19b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table()


def downgrade() -> None:
    pass
