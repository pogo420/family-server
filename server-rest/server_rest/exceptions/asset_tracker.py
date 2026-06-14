"""Exceptions for AssetTracker related errors."""


class AssetTrackerException(Exception):
    """Base exception class for AssetTracker related errors."""

    pass


class AssetAlreadyExistsException(AssetTrackerException):
    """Exception raised when trying to add an asset that already exists."""

    pass


class AssetDeleteException(AssetTrackerException):
    """Exception raised when an asset cannot be deleted."""

    pass


class AssetRetrieveException(AssetTrackerException):
    """Exception raised when there is an error retrieving an asset."""

    pass


class AssetAddException(AssetTrackerException):
    """Exception raised when there is an error adding an asset."""

    pass
