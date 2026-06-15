"""Logic for config setup"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class for config"""

    APP_NAME: str
    DB_URL: str
    ENABLE_DEBUG: bool
    MQTT_CLIENT_ID: str
    MQTT_HOST: str
    MQTT_PORT: int
    MQTT_USERNAME: str
    MQTT_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    """Function to return app settings.
    Function is cached, to prevent reading of filesystem.
    """
    return Settings()
