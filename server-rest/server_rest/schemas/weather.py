"""Schemas for weather readings."""

from pydantic import BaseModel, Field


class WeatherReadingPayload(BaseModel):
    """Schema for weather reading payload."""

    temperature: float = Field(ge=-50, le=100)
    humidity: float = Field(ge=0, le=100)
    pressure: float = Field(ge=300, le=1200)
