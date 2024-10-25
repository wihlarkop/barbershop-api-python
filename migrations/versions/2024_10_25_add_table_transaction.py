"""add table transaction

Revision ID: 8cf239a8826f
Revises: 94992a42f35b
Create Date: 2024-10-25 23:07:17.774686

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.helper.generator import timezone
from app.models.transaction import PaymentMethodEnum

# revision identifiers, used by Alembic.
revision: str = '8cf239a8826f'
down_revision: Union[str, None] = '94992a42f35b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

enforce_capster_role_create = """
        CREATE FUNCTION enforce_capster_role() 
        RETURNS TRIGGER AS $$
        BEGIN
            IF (SELECT user_role FROM "user" WHERE uuid = NEW.capster_uuid) != 'capster' THEN
                RAISE EXCEPTION 'Only users with role capster can be assigned as capsters.';
            END IF;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """

enforce_capster_role_trigger_create = """
        CREATE TRIGGER enforce_capster_role_trigger
        BEFORE INSERT OR UPDATE ON transaction
        FOR EACH ROW EXECUTE FUNCTION enforce_capster_role();
    """

enforce_capster_role_drop = "DROP TRIGGER IF EXISTS enforce_capster_role_trigger ON transaction;"

enforce_capster_role_trigger_drop = "DROP FUNCTION IF EXISTS enforce_capster_role;"

def upgrade() -> None:
    op.create_table(
        "transaction",
        sa.Column(name="uuid", type_=sa.UUID(), primary_key=True),
        sa.Column(name="user_uuid", type_=sa.UUID()),
        sa.Column(name="store_uuid", type_=sa.UUID()),
        sa.Column(name="capster_uuid", type_=sa.UUID()),
        sa.Column(name="product_uuid", type_=sa.UUID()),
        sa.Column(
            name="payment_method",
            type_=sa.Enum("cash", "debit", "credit", "e_wallet",name="payment_method_enum"),
            nullable=False
        ),
        sa.Column(name="created_at", type_=sa.TIMESTAMP(timezone=True), default=datetime.now(tz=timezone)),
        sa.Column(name="updated_at", type_=sa.TIMESTAMP(timezone=True), onupdate=datetime.now(tz=timezone)),
        sa.Column(name="deleted_at", type_=sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column(name="created_by", type_=sa.String(length=255)),
        sa.Column(name="updated_by", type_=sa.String(length=255)),
        sa.Column(name="deleted_by", type_=sa.String(length=255)),

        sa.ForeignKeyConstraint(name="fk_transaction_user", columns=["user_uuid"], refcolumns=["user.uuid"]),
        sa.ForeignKeyConstraint(name="fk_transaction_store", columns=["store_uuid"], refcolumns=["store.uuid"]),
        sa.ForeignKeyConstraint(name="fk_transaction_capster", columns=["capster_uuid"], refcolumns=["user.uuid"]),
        sa.ForeignKeyConstraint(name="fk_transaction_product", columns=["product_uuid"], refcolumns=["product.uuid"]),

    )
    op.execute(enforce_capster_role_create)
    op.execute(enforce_capster_role_trigger_create)


def downgrade() -> None:
    op.drop_table(table_name="transaction")
    op.execute(enforce_capster_role_drop)
    op.execute(enforce_capster_role_trigger_drop)
    payment_method_enum = sa.Enum(name="payment_method_enum")
    payment_method_enum.drop(op.get_bind())