import random


class Hat:
    houses = ["Gryffindor", "HufflePuff", "RavenClaw", "Slytherin"]

    # class variable
    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")


Hat.sort("Harry")
