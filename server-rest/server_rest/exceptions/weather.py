class WeatherApiException(Exception):
    """Base exception class for Weather API related errors."""

    pass


class WeatherReadingsAddException(WeatherApiException):
    """Exception raised when adding weather readings fails."""

    pass
