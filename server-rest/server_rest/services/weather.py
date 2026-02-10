from server_rest.models.weather import WeatherData
from server_rest.schemas.weather import WeatherDataPayload
from server_rest.repository.weather import add_weather as add_weather_to_db

from datetime import datetime
from sqlalchemy.orm import Session


def add_weather(db: Session, weather_data_payload: WeatherDataPayload):
    weather_data = WeatherData(
        dt=datetime.strptime(
            weather_data_payload.date_time, "%Y-%m-%d %H:%M:%S"),
        pressure=weather_data_payload.pressure,
        temperature=weather_data_payload.temperature,
        humidity=weather_data_payload.humidity
    )

    if not add_weather_to_db(db, weather_data):
        raise Exception("issue in adding data to db")
