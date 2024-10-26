from faker import Faker

from app.entities.store import StoreEntities
from app.helper.generator import generate_uuid
from sqlalchemy import URL, text, insert
from sqlalchemy.engine import create_engine

from app.models.store import store

fake = Faker()


def generate_fake_store():
    url = URL.create(
        drivername="postgresql+psycopg",
        username="postgres",
        password="admin",
        host="localhost",
        port=5432,
        database="barbershop",
    )
    engine = create_engine(
        url=url
    )
    stores = [
        StoreEntities(
            created_at=fake.date_time(),
            created_by=fake.name(),
            uuid=generate_uuid(),
            store_name=fake.company(),
            address=fake.address(),
            phone_number=fake.phone_number(),
            opening_hours=fake.time(pattern="%H:%M:%S"),
            closing_hours=fake.time(pattern="%H:%M:%S")
        ).model_dump() for _ in range(5)
    ]

    with engine.connect() as connection:
        check_store = connection.execute(text("select count(uuid) from store"))
        print(check_store.fetchone())
        if check_store.fetchone() < 0:
            insert(store).values(stores)

if __name__ == '__main__':
    generate_fake_store()