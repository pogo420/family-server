from pydantic import BaseModel, field_validator, Field
from datetime import datetime


class WeatherDataPayload(BaseModel):
    date_time: str = Field(
        description="Date time in following format: %Y-%m-%d %H:%M:%S")
    location: str = Field(
        description="Location of sensor, example: High garden, Kochi"
    )
    pressure: float
    temperature: float
    humidity: float

    @field_validator("date_time")
    @classmethod
    def date_time_format_check(cls, dt: str) -> str:
        try:
            datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise
        else:
            return dt
