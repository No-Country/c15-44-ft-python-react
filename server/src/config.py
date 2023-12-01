from functools import lru_cache

from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    database_url: SecretStr
    secret: SecretStr
    password_reset_secret: SecretStr
    verification_secret: SecretStr

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()  # type: ignore
