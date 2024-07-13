from sqlalchemy import URL, MetaData
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.config import settings
from app.helper.generator import build_connection_url


class DatabaseClient:
    def __init__(self, database_connection_url: str | URL):
        self.connection_url = database_connection_url

    def create_engine(self) -> AsyncEngine:
        return create_async_engine(
            url=self.connection_url,
            pool_pre_ping=True,
            # echo=True,
            # echo_pool=True
        )

    def get_meta_data(self) -> MetaData:
        return MetaData()


connection_url = build_connection_url(
    driver_name="postgresql+psycopg",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    database=settings.POSTGRES_DB
)

client = DatabaseClient(database_connection_url=connection_url)
engine = client.create_engine()
metadata = client.get_meta_data()
