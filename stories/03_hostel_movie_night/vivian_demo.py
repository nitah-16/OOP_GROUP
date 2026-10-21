
from story import BoardGame, Entertainment, MovieNight, StreamedMovie, show_options
class Ludo(BoardGame):
    title = "Ludo"

def main():
    ludo = Ludo()
    movie = StreamedMovie("Mukono Mystery")

    print("Is Ludo an Entertainment?", isinstance(ludo, Entertainment))
    show_options([movie, ludo])

    david = MovieNight("David", 200)
    print(david.enjoy(movie))
    print(david.enjoy(ludo))
    print(f"David: {david.bundle.remaining} MB left; activities: {david.activities}")


if __name__ == "__main__":
    main()