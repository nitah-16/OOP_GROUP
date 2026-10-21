from errors import MovieChoiceError, MovieRequestError, MovieResourceError
from story import StreamedMovie, MusicSession, StorytellingCircle
from strict_night import StrictMovieNight


class BrokenQuote:  # fake choice with a negative requirement
    title = "Broken quote"

    def data_cost(self):
        return -50


night = StrictMovieNight("Faith", 500)
attempts = [None, BrokenQuote(), StreamedMovie("Big Film"),
            MusicSession("Afrobeats"), StorytellingCircle()]

for choice in attempts:
    try:
        print(night.safe_enjoy(choice))
    except MovieChoiceError as e:
        print("Please pick something first:", e)
    except MovieRequestError as e:
        print("That request doesn't make sense:", e)
    except MovieResourceError as e:
        print("Not enough data:", e)
    finally:
        print(f"-- attempt finished (remaining {night.bundle.remaining} MB, "
              f"activities {night.activities})\n")