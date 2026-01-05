from sqlalchemy import Column, Float, DateTime
from server_rest.db.database import Base


class WeatherData(Base):
    __tablename__ = "weather_data"

    dt = Column(DateTime, primary_key=True, nullable=False, index=True)
    pressure = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
