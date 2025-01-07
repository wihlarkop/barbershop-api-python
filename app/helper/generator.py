import random
import string
from datetime import datetime
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo

from passlib.hash import pbkdf2_sha256
from sqlalchemy import URL

timezone = ZoneInfo("Asia/Jakarta")


def build_connection_url(
    driver_name: str,
    username: str,
    password: str,
    host: str,
    port: str | int,
    database: str,
) -> URL:
    return URL.create(
        drivername=driver_name,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )


def generate_time_now():
    return datetime.now(tz=timezone)


def generate_uuid() -> UUID:
    return uuid4()


def generate_random_string(length: int) -> str:
    """
    Generate a random string with the specified length.

    Args:
        length (int): The length of the random string to generate.

    Returns:
        str: A randomly generated string with the specified length.
    """
    if length <= 0:
        raise ValueError("Length must be greater than 0.")

    characters = string.ascii_letters + string.digits  # Includes a-z, A-Z, and 0-9
    return "".join(random.choices(characters, k=length))


async def hash_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)


async def verify_password(password: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(password, hashed_password)


async def generate_access_token():
    pass


async def decode_access_token(token: str):
    pass
