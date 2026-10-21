from errors import MovieChoiceError, MovieRequestError, MovieResourceError
from story import StreamedMovie, MusicSession, StorytellingCircle
from strict_night import StrictMovieNight


class FakeChoice:
    def __init__(self, cost, title="Fake"):
        self.title = title
        self._cost = cost

    def data_cost(self):
        return self._cost


def snapshot(night):
    return (night.bundle.remaining, night.activities, night.entertainment)


def expect_failure(night, choice, error_type):
    before = snapshot(night)
    try:
        night.safe_enjoy(choice)
        assert False, "expected an error"
    except error_type:
        pass
    assert snapshot(night) == before  # nothing spent or recorded


def test_choice_error():
    expect_failure(StrictMovieNight("F", 500), None, MovieChoiceError)


def test_request_error():
    expect_failure(StrictMovieNight("F", 500), FakeChoice(-10), MovieRequestError)


def test_resource_error():
    expect_failure(StrictMovieNight("F", 500), StreamedMovie("Big"), MovieResourceError)


def test_valid_succeeds():
    n = StrictMovieNight("F", 500)
    n.safe_enjoy(MusicSession("Beats"))
    assert n.bundle.remaining == 400 and n.activities == 1


def test_zero_cost_is_valid_not_missing():
    n = StrictMovieNight("F", 500)
    n.safe_enjoy(StorytellingCircle())
    assert n.bundle.remaining == 500 and n.activities == 1


def test_exact_remaining_is_allowed():
    n = StrictMovieNight("F", 100)
    n.safe_enjoy(MusicSession("Beats"))
    assert n.bundle.remaining == 0 and n.activities == 1


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)