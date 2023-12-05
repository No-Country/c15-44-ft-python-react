from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings
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
