from datetime import datetime, timedelta

import jwt

from app.config import settings
from app.exceptions.token_exception import TokenExpired, TokenInvalid


def generate_jwt(email: str) -> str:
    payload = {
        "email": email,
        "exp": datetime.now() + timedelta(days=1)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


def generate_refresh_token(email) -> str:
    payload = {
        "email": email,
        "exp": datetime.now() + timedelta(days=7)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


def refresh_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return generate_jwt(payload.get('email'))
    except jwt.ExpiredSignatureError:
        raise TokenExpired()
    except jwt.InvalidTokenError:
        raise TokenInvalid()
