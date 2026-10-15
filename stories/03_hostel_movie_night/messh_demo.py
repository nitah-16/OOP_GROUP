
from story import DataSaverMovie, MovieNight, TinyMovie, show_options


normal_movie = TinyMovie("Tiny Mystery")
boundary_movie = TinyMovie("Three-MB Tiny Movie", megabytes=3)

show_options([normal_movie, boundary_movie])

print("Normal case: default 700 MB movie")
print("Expected cost: 175 MB")
print(f"Actual cost:   {normal_movie.data_cost()} MB")
normal_night = MovieNight("Messh", 200)
expected_result = "Messh's group enjoys Tiny Mystery."
actual_result = normal_night.enjoy(normal_movie)
print(f"Expected result: {expected_result}")
print(f"Actual result:   {actual_result}")
print("Expected data left: 25 MB")
print(f"Actual data left:   {normal_night.bundle.remaining} MB")

print("\nBoundary case: 3 MB source uses integer division")
parent_movie = DataSaverMovie("Three-MB parent", megabytes=3)
print(f"Expected parent cost: 1 MB; actual: {parent_movie.data_cost()} MB")
print("Expected TinyMovie cost: 0 MB")
print(f"Actual TinyMovie cost:   {boundary_movie.data_cost()} MB")
boundary_night = MovieNight("Messh", 1)
expected_result = "Messh's group enjoys Three-MB Tiny Movie."
actual_result = boundary_night.enjoy(boundary_movie)
print(f"Expected result: {expected_result}")
print(f"Actual result:   {actual_result}")
print("Expected data left: 1 MB")
print(f"Actual data left:   {boundary_night.bundle.remaining} MB")
