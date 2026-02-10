from server_rest.models.weather import WeatherData
from sqlalchemy.orm import Session


def add_weather(
        db: Session,
        weather_data: WeatherData) -> WeatherData | None:
    try:
        db.add(weather_data)
        db.commit()
        db.refresh(weather_data)
        return weather_data
    except Exception:
        return None
