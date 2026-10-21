class MovieChoiceError(Exception):
    """No choice object was supplied (None)."""


class MovieRequestError(Exception):
    """The request is invalid, e.g. a negative requirement."""


class MovieResourceError(Exception):
    """The request is valid but needs more MB than remain."""