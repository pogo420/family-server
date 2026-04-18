import logging
import uuid

from server_rest.exceptions.event_tracker import EventAlreadyExistsException
from server_rest.schemas.common import GenericMessage
from server_rest.schemas.event_tracker import Event, EventFilter, EventResponse
from server_rest.models.event_tracker import EventTracker
from server_rest.repository.event_tracker import add_event, delete_event, get_events_by_date


# Local file logger
logger = logging.getLogger(__name__)


def add_event_service(db, event_data: Event) -> GenericMessage:
    """Service function to add a new event to the database.
    Args:
        db: Database session.
        event_data (Event): Event data to be added.
    Returns:
        GenericMessage: A generic message indicating the result of the operation.
    """

    event_table_row = EventTracker(
        event_name=event_data.event_name,
        day=event_data.day,
        month=event_data.month,
        event_id=uuid.uuid4().hex
    )
    try:
        db_response = add_event(db, event_table_row)
        return {"message": f"Event '{db_response.event_name}' added for {db_response.day}/"
                           f"{db_response.month}, id: {db_response.event_id}"}
    except EventAlreadyExistsException:
        return {"message": f"Event already exists for day: {event_data.day}, month: {event_data.month}, "
                           f"name: {event_data.event_name}"}
    except Exception as e:
        return {"message": f"Error adding event: {e}"}


def delete_event_service(db, event_id: str) -> GenericMessage:
    """Service function to delete an event from the database by its ID.
    Args:
        db: Database session.
        event_id (str): ID of the event to be deleted.
    Returns:
        GenericMessage: A generic message indicating the result of the operation.
    """
    try:
        success = delete_event(db, event_id)
        if success:
            return {"message": f"Event with ID '{event_id}' deleted successfully."}
        else:
            return {"message": f"Event with ID '{event_id}' not found."}
    except Exception as e:
        return {"message": f"Error deleting event with ID '{event_id}': {e}"}


def get_events_by_date_service(db, event_filter: EventFilter) -> list[EventResponse]:
    """Service function to retrieve events from the database based on the provided date filter.
    Args:
        db: Database session.
        event_filter (EventFilter): Filter criteria for retrieving events.
    Returns:
        list[EventResponse]: A list of events matching the filter criteria, empty if no matches found.
    """
    try:
        events = get_events_by_date(db, event_filter)
        return [EventResponse(
            event_id=event.event_id,
            day=event.day,
            month=event.month,
            event_name=event.event_name
        ) for event in events]
    except Exception as e:
        logger.error(f"Error retrieving events for day: {event_filter.day}, month: {event_filter.month}: {e}")
        return []
