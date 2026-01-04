from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    DB_URL: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    """Function to return app settings.
    Function is cached, to prevent reading of filesystem.
    """
    return Settings()
