"""Repository module for weather readings."""

import logging

from server_rest.exceptions.weather import WeatherReadingsAddException
from server_rest.models.weather import WeatherReadings

logger = logging.getLogger(__name__)


def add_weather_reading(db, device_id, timestamp, temperature, humidity, pressure) -> None:
    """Repository function to add a weather reading to the database.
    Args:
        db: Database session.
        device_id (str): ID of the device submitting the weather reading.
        timestamp (datetime): Timestamp of the weather reading.
        temperature (float): Temperature reading.
        humidity (float): Humidity reading.
        pressure (float): Pressure reading.
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    try:
        new_reading = WeatherReadings(
            device_id=device_id, timestamp=timestamp, temperature=temperature, humidity=humidity, pressure=pressure
        )
        db.add(new_reading)
        db.commit()
        db.refresh(new_reading)
        logger.info(f"Weather reading added: {new_reading}")
    except Exception as e:
        logger.error(f"Error adding weather reading: {e}")
        db.rollback()
        raise WeatherReadingsAddException from e
