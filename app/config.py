from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_NAME: str
    APP_ENV: str = "local"
    APP_VERSION: str = "local"
    HOST: str = "0.0.0.0"
    PORT: int = 8088
    DEBUG: bool = 0
    SECRET_KEY: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    POOL_RECYCLE: int
    POOL_TIMEOUT: int
    POOL_SIZE: int
    MAX_OVERFLOW: int


settings = Settings()
