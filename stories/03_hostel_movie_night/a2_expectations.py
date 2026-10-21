# stories/03_hostel_movie_night/a2_exceptions.py

class MovieChoiceError(Exception):
    """Raised when no choice object was supplied (None)."""
    pass

class MovieRequestError(Exception):
    """Raised for an invalid request, such as a negative calculated requirement."""
    pass

class MovieResourceError(Exception):
    """Raised when the request is valid but needs more MB than remain."""
    pass