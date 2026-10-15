from story import Entertainment


class ComedyClip(Entertainment):
    def __init__(self, title):
        self.title = title

    def data_cost(self):
        return 50


clip = ComedyClip("Short comedy clip")

print("ComedyClip is an Entertainment that costs 50 MB")
print("Is an Entertainment?", isinstance(clip, Entertainment))
print("Data cost:", clip.data_cost(), "MB")
print(f"{clip.title} uses {clip.data_cost()} MB of data.")

print("\nMRO:", " -> ".join(c.__name__ for c in ComedyClip.__mro__))