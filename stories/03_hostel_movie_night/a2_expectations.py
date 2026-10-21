# stories/03_hostel_movie_night/a2_exceptions.py

#Short Explanation for Option A2 (Custom Exceptions):
#This module defines custom exception classes for the Hostel Movie Night project:
#- MovieChoiceError: Raised when no choice object is provided (None).
#- MovieRequestError: Raised when a request contains invalid data (such as negative MB).
#- MovieResourceError: Raised when a request exceeds the remaining MB resources.
#These custom exceptions provide clear, descriptive error handling for strict validation.

class MovieChoiceError(Exception):
    "Raised when no choice object was supplied (None)."
    pass

class MovieRequestError(Exception):
    "Raised for an invalid request, such as a negative calculated requirement."
    pass

class MovieResourceError(Exception):
    "Raised when the request is valid but needs more MB than remain."
    pass