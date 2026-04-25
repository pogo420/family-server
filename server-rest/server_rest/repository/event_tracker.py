"""Repository for EventTracker model.
Raw SQL queries and database operations related to EventTracker can be defined here.
"""
from sqlalchemy.orm import Session
from typing import Optional
import logging

from server_rest.exceptions.event_tracker import EventAlreadyExistsException
from server_rest.schemas.event_tracker import EventFilter
from server_rest.models.event_tracker import EventTracker


# Local file logger
logger = logging.getLogger(__name__)


def add_event(db: Session, event: EventTracker) -> Optional[EventTracker]:
    """Add a new event to the database.
    Args:
        db (Session): Database session.
        event (EventTracker): Event data to be added.
    Returns:
        Optional[EventTracker]: The added event if successful, None otherwise.
    Rasises:
        EventAlreadyExistsException: If an event with the same name, day, and month already exists.
        Exception: If there is an error during the database operation.
    """
    try:
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
    except Exception as e:
        db.rollback()
        logger.error(f"Error adding event: {e}")
        if "violates unique constraint" in str(e):
            raise EventAlreadyExistsException()
        raise


def delete_event(db: Session, event_id: str):
    """Delete an event from the database by its ID.
    Args:
        db (Session): Database session.
        event_id (str): ID of the event to be deleted.
    Returns:
        bool: True if the event was deleted, False if the event was not found.
    Raises:
        Exception: If there is an error during the database operation.
    """
    try:
        event = db.query(EventTracker).filter(EventTracker.event_id == event_id).first()
        if event:
            db.delete(event)
            db.commit()
            return True
        else:
            logger.warning(f"Event with ID '{event_id}' not found for deletion.")
            return False
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting event with ID '{event_id}': {e}")
        raise


def get_events_by_date(db: Session, date: EventFilter) -> list[EventTracker]:
    """Retrieve events from the database that match the specified date.
    Args:
        db (Session): Database session.
        date (EventFilter): Date filter containing day and month.
    Returns:
        list[EventTracker]: List of events that match the specified date.
    Raises:
        Exception: If there is an error during the database operation.
    """
    try:
        events = db.query(EventTracker).filter(
            EventTracker.day == date.day,
            EventTracker.month == date.month
        ).all()
        return events
    except Exception as e:
        logger.error(f"Error retrieving events for date {date}: {e}")
        raise


def get_all_events(db: Session) -> list[EventTracker]:
    """Retrieve all events from the database.
    Args:
        db (Session): Database session.
    Returns:
        list[EventTracker]: List of all events in the database.
    Raises:
        Exception: If there is an error during the database operation.
    """
    try:
        events = db.query(EventTracker).all()
        return events
    except Exception as e:
        logger.error(f"Error retrieving all events: {e}")
        raise
