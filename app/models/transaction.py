from datetime import datetime
from enum import StrEnum

from sqlalchemy import Column, DDL, Enum, event, ForeignKeyConstraint, String, Table, TIMESTAMP, UUID

from app.database.client import metadata
from app.helper.generator import timezone


class PaymentMethodEnum(StrEnum):
    cash = "cash"
    debit = "debit"
    credit = "credit"
    e_wallet = "e_wallet"


transaction = Table(
    "transaction",
    metadata,
    Column(name="uuid", type_=UUID(), primary_key=True),
    Column(name="user_uuid", type_=UUID()),
    Column(name="store_uuid", type_=UUID()),
    Column(name="capster_uuid", type_=UUID()),
    Column(name="product_uuid", type_=UUID()),
    Column(name="payment_method", type_=Enum(PaymentMethodEnum), nullable=False),
    Column(name="created_at", type_=TIMESTAMP(timezone=True), default=datetime.now(tz=timezone)),
    Column(name="updated_at", type_=TIMESTAMP(timezone=True), onupdate=datetime.now(tz=timezone)),
    Column(name="deleted_at", type_=TIMESTAMP(timezone=True), nullable=True),
    Column(name="created_by", type_=String(length=255)),
    Column(name="updated_by", type_=String(length=255)),
    Column(name="deleted_by", type_=String(length=255)),

    ForeignKeyConstraint(name="fk_transaction_user", columns=["user_uuid"], refcolumns=["user.uuid"]),
    ForeignKeyConstraint(name="fk_transaction_store", columns=["store_uuid"], refcolumns=["store.uuid"]),
    ForeignKeyConstraint(name="fk_transaction_capster", columns=["capster_uuid"], refcolumns=["user.uuid"]),
    ForeignKeyConstraint(name="fk_transaction_product", columns=["product_uuid"], refcolumns=["product.uuid"]),
)

capster_func = DDL(
    """
    CREATE FUNCTION enforce_capster_role() 
    RETURNS TRIGGER AS $$
    BEGIN
        IF (SELECT user_role FROM user WHERE uuid = NEW.capster_uuid) != 'capster' THEN
            RAISE EXCEPTION 'Only users with role capster can be assigned as capsters.';
        END IF;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """
)

capster_trigger = DDL(
    """
    CREATE TRIGGER enforce_capster_role_trigger
    BEFORE INSERT OR UPDATE ON transaction
    FOR EACH ROW EXECUTE FUNCTION enforce_capster_role();
    """
)

event.listen(transaction, "after_create", capster_func.execute_if(dialect="postgresql"))
event.listen(transaction, "after_create", capster_trigger.execute_if(dialect="postgresql"))
