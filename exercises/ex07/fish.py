"""File to define Fish class."""

__author__ = "730742450"


class Fish:
    """Fish class with an age attribute."""

    age: int

    def __init__(self):
        """Initializes a fish object."""
        self.age = 0
        return None

    def one_day(self):
        """Adds 1 to age of fish."""
        self.age += 1
        return None
