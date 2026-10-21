from errors import MovieChoiceError, MovieRequestError, MovieResourceError
from story import MovieNight


class StrictMovieNight(MovieNight):
    """A MovieNight that checks a request before spending or recording anything."""

    def safe_enjoy(self, choice):
        if choice is None:  
            raise MovieChoiceError("No choice was supplied.")
        needed = choice.data_cost()
        if needed < 0:
            raise MovieRequestError(f"Invalid requirement: {needed} MB.")
        if needed > self.bundle.remaining:
            raise MovieResourceError(
                f"{choice.title} needs {needed} MB but only "
                f"{self.bundle.remaining} MB remain.")
        return self.enjoy(choice)  