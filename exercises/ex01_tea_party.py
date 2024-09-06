"""Using # of guests, calculates needed # of teabags and treats, and total cost"""

__author__ = "730742450"


def main_planner(guests: int) -> None:
    """Prints calculated information about tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats " + str(treats(people=guests)))
    print(
        "Cost: "
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """calculates number of teabags needed"""
    return people * 2


def treats(people: int) -> int:
    """calculates number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates cost of teabags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
