from uuid import uuid4, UUID
from zoneinfo import ZoneInfo

from sqlalchemy import URL


def build_connection_url(
        driver_name: str,
        username: str,
        password: str,
        host: str,
        port: str | int,
        database: str
) -> URL:
    return URL.create(
        drivername=driver_name,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )


def generate_uuid() -> UUID:
    return uuid4()


timezone = ZoneInfo("Asia/Jakarta")
