"""Route for db connection check
"""
from fastapi import APIRouter, Depends
import logging
from sqlalchemy.orm import Session

from server_rest.schemas.common import GenericMessage
from server_rest.db.database import get_db
from server_rest.services.db_test import is_db_alive

# Local file logger
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/db-test",
    tags=["db test"]
)


@router.get("/", response_model=GenericMessage)
def db_test(db: Session = Depends(get_db)):
    logger.info("Handling db test endpoint")
    if is_db_alive(db):
        return {"message": "DB is alive"}
    else:
        return {"message": "DB is dead"}
