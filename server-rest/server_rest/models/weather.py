"""Model for weather readings."""

from sqlalchemy import Column, DateTime, Float, Index, Integer, String

from server_rest.db.database import Base


class WeatherReadings(Base):
    __tablename__ = "weather_readings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(100), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    temperature = Column(Float, nullable=False)  # Temperature in Celsius
    humidity = Column(Float, nullable=False)  # Humidity in percentage
    pressure = Column(Float, nullable=False)  # Pressure in hPa

    __table_args__ = (
        Index(
            "idx_weather_device_timestamp",
            "device_id",
            "timestamp",
        ),
    )
