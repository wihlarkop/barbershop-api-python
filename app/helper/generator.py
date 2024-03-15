from uuid import uuid4, UUID
from zoneinfo import ZoneInfo

from sqlalchemy import URL
from passlib.hash import pbkdf2_sha256

timezone = ZoneInfo("Asia/Jakarta")


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


async def hash_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)


async def verify_password(password: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(password, hashed_password)


async def generate_access_token():
    pass


async def decode_access_token(token: str):
    pass
