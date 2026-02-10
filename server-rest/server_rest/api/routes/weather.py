from fastapi import APIRouter, Depends
from server_rest.schemas.common import GenericMessage
from server_rest.schemas.weather import WeatherDataPayload
from server_rest.services.weather import add_weather
from sqlalchemy.orm import Session
from server_rest.db.database import get_db


router = APIRouter(
    prefix="/weather",
    tags=["Weather Api"],
    dependencies=[Depends(get_db)]  # router level dependencies
)


@router.get("/", response_model=GenericMessage)
def read_weather(db: Session = Depends(get_db)):
    return {"message": "Endpoint in progress"}


@router.post("/", response_model=GenericMessage)
def write_weather(payload: WeatherDataPayload, db: Session = Depends(get_db)):
    try:
        add_weather(db, payload)
    except Exception as e:
        return {"message": f"Issue in adding data {payload.model_dump_json()},"
                           f" details: {e}"}
    else:
        return {"message": f"Data {payload.model_dump_json()} added successfully"}
