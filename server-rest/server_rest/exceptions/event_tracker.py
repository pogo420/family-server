"""Exceptions for EventTracker related errors."""


class EventTrackerException(Exception):
    """Base exception class for EventTracker related errors."""
    pass


class EventAlreadyExistsException(EventTrackerException):
    """Exception raised when trying to add an event that already exists."""
    pass
