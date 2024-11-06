"""File to define River class."""

__author__ = "730742450"
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class with day, fish, and bears attributes."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes overaged animals."""
        # new lists to hold surviving animals
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []

        for fish in self.fish:
            # adds surviving fish to new list
            if fish.age <= 3:
                surviving_fish.append(fish)

        for bear in self.bears:
            # adds surviving bears to new list
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """Updates fish count and bear hunger score to reflect bear eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                # removes 3 fish if there are at least 5 fish for current bear
                self.remove_fish(3)
                # adds 3 to bear hunger_score
                bear.eat(3)
        return None

    def check_hunger(self):
        """Removes bears if they're too hungry."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Adds 4 fish for every existing pair of fish."""
        num_fishies = (len(self.fish) // 2) * 4
        i = 0
        while i < num_fishies:
            self.fish.append(Fish())
            i += 1
        return None

    def repopulate_bears(self):
        """Adds a bear for each pair of current bears."""
        num_cubs = len(self.bears) // 2
        i = 0
        while i < num_cubs:
            self.bears.append(Bear())
            i += 1
        return None

    def view_river(self):
        """Displays info about river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Run one_river_day 7 times."""
        i = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None

    def remove_fish(self, amount: int):
        """Removes specified number of fish."""
        count = 0
        while count < amount:
            # removes fish at first index
            self.fish.pop(0)
            count += 1
        return None
