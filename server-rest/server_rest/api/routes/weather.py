from fastapi import APIRouter, Depends
from server_rest.schemas.common import GenericMessage
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
