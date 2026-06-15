"""MQTT handlers for processing incoming messages."""

import logging

from pydantic_core import ValidationError
from server_rest.exceptions.weather import WeatherReadingsAddException
from server_rest.schemas.weather import WeatherReadingPayload
from server_rest.services.weather import add_weather_reading_service

logger = logging.getLogger(__name__)


def handler_weather_update(device_id: str, payload: dict) -> None:
    logger.debug(f"Received weather update for device {device_id}: {payload}")
    try:
        payload = WeatherReadingPayload.model_validate(payload)
    except ValidationError:
        logger.error(f"Invalid weather payload received from device {device_id}")
        return
    logger.info(f"Valid weather reading received from device {device_id}: {payload}")
    try:
        add_weather_reading_service(device_id, payload)
    except WeatherReadingsAddException:
        logger.error(f"Failed to add weather reading for device {device_id}")
        return
