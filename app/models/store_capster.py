from sqlalchemy import Table, Column, UUID, ForeignKeyConstraint

from app.database.client import metadata

store_capster = Table(
    "store_capster",
    metadata,
    Column(name="uuid", type_=UUID(), primary_key=True),
    Column(name="user_uuid", type_=UUID()),
    Column(name="store_uuid", type_=UUID()),

    ForeignKeyConstraint(name="fk_store_capster_user", columns=["user_uuid"], refcolumns=["user.uuid"]),
    ForeignKeyConstraint(name="fk_store_capster_store", columns=["store_uuid"], refcolumns=["store.uuid"]),
)
