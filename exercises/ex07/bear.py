"""File to define Bear class."""

__author__ = "730742450"


class Bear:
    """Bear class with an age and hunger_score attribute."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes a bear object."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Updates age by 1, decreases hunger by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increases hunger score by specified amount."""
        self.hunger_score += num_fish
        return None
