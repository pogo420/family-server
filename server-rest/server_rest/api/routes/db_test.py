from fastapi import APIRouter, Depends
from server_rest.schemas.common import GenericMessage
from sqlalchemy.orm import Session
from server_rest.db.database import get_db
from server_rest.services.db_test import is_db_alive


router = APIRouter(
    prefix="/db-test",
    tags=["db test"]
)


@router.get("/", response_model=GenericMessage)
def db_test(db: Session = Depends(get_db)):
    if is_db_alive(db):
        return {"message": "DB is alive"}
    else:
        return {"message": "DB is dead"}
