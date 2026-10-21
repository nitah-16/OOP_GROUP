"""A3: Save and load a Hostel Movie Night session as JSON (no eval)."""
import json
from story import (
    MovieNight, StreamedMovie, MusicSession, ComedyClip,
    DataSaverMovie, FeaturedMovie, StorytellingCircle, BoardGame,
)

# Secure type map: only these classes can ever be rebuilt from a save file.
TYPE_MAP = {
    cls.__name__: cls
    for cls in (StreamedMovie, MusicSession, ComedyClip, DataSaverMovie,
                FeaturedMovie, StorytellingCircle, BoardGame)
}


def entertainment_to_dict(item):
    data = {"type": type(item).__name__, "title": item.title}
    if isinstance(item, StreamedMovie):  # also covers DataSaverMovie, FeaturedMovie
        data["megabytes"] = item.megabytes
    return data


def entertainment_from_dict(data):
    cls = TYPE_MAP.get(data.get("type"))
    if cls is None:
        raise ValueError(f"Unknown type in save file: {data.get('type')!r}")
    if cls in (StorytellingCircle, BoardGame):  # take no constructor arguments
        return cls()
    if issubclass(cls, StreamedMovie):
        return cls(data["title"], data.get("megabytes", 700))
    return cls(data["title"])


def save_session(path, nights, resources):
    session = {
        "students": [
            {"host": n.host, "remaining": n.bundle.remaining} for n in nights
        ],
        "resources": [entertainment_to_dict(r) for r in resources],
        "history": [
            {"host": n.host, "activity": entertainment_to_dict(a)}
            for n in nights for a in n._watched
        ],
    }
    with open(path, "w") as f:
        json.dump(session, f, indent=2)


def load_session(path):
    try:
        with open(path) as f:
            session = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Save file not found: {path}")
    except json.JSONDecodeError:
        raise ValueError("Save file is corrupted or not valid JSON.")

    nights = {s["host"]: MovieNight(s["host"], s["remaining"])
              for s in session["students"]}
    resources = [entertainment_from_dict(r) for r in session["resources"]]
    for entry in session["history"]:
        nights[entry["host"]]._watched.append(
            entertainment_from_dict(entry["activity"])
        )
    return list(nights.values()), resources


if __name__ == "__main__":
    options = [StreamedMovie("Mukono Mystery"), MusicSession("Afrobeats break"),
               FeaturedMovie("Mukono Mystery: data saver"), BoardGame()]
    faith = MovieNight("Faith", 500)
    david = MovieNight("David", 200)
    faith.enjoy(options[2])
    david.enjoy(options[1])

    save_session("session.json", [faith, david], options)
    nights, resources = load_session("session.json")
    for n in nights:
        print(n.host, n.bundle.remaining, n.activities)