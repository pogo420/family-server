"""Service layer for weather-related operations."""

import logging
from datetime import UTC, datetime

from server_rest.db.database import SessionLocal
from server_rest.repository.weather import add_weather_reading
from server_rest.schemas.weather import WeatherReadingPayload

logger = logging.getLogger(__name__)


def add_weather_reading_service(device_id: str, weather_reading_payload: WeatherReadingPayload) -> None:
    """Service function to add a weather reading to the database.
    Args:
        db: Database session.
        device_id (str): ID of the device submitting the weather reading.
        weather_reading_payload (WeatherReadingPayload): Payload containing weather reading data.
    Returns:
        GenericMessage: A generic message indicating the result of the operation.
    """
    try:
        with SessionLocal() as db:
            db_response = add_weather_reading(
                db,
                device_id,
                datetime.now(UTC),
                weather_reading_payload.temperature,
                weather_reading_payload.humidity,
                weather_reading_payload.pressure,
            )
        logger.info(f"Weather reading added for device {device_id}: {db_response}")
    except Exception as e:
        logger.error(f"Error adding weather reading for device {device_id}: {e}")
        raise e
