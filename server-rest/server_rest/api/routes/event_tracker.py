"""Routes for event tracker API
"""
from fastapi import APIRouter, Depends
import logging
from sqlalchemy.orm import Session

from server_rest.schemas.common import GenericMessage
from server_rest.db.database import get_db
from server_rest.schemas.event_tracker import Event, EventFilter, EventResponse
from server_rest.services.event_tracker import add_event_service, delete_event_service, get_events_by_date_service


# Local file logger
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/event-tracker",
    tags=["event tracker"]
)


@router.get("/", response_model=list[EventResponse])
def show_events(
    event_filter: EventFilter = Depends(),
    db: Session = Depends(get_db)
):
    logger.info(f"Searching for events with filter: day={event_filter.day}, month={event_filter.month}")
    return get_events_by_date_service(db, event_filter)


@router.post("/", response_model=GenericMessage)
def add_event(
    event: Event,
    db: Session = Depends(get_db)
):
    logger.info(f"Adding event: {event}")
    return add_event_service(db, event)


@router.delete("/", response_model=GenericMessage)
def delete_event(
    event_id: str,
    db: Session = Depends(get_db)
):
    logger.info(f"Deleting event with ID: {event_id}")
    return delete_event_service(db, event_id)
