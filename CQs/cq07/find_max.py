"""holds function to find and remove + return max value in a list"""

__author__ = "730742450"


def find_and_remove_max(the_list: list[int]) -> int:
    """Finds, returns, and removes the max value in the list"""
    if len(the_list) == 0:
        return -1
    max: int = the_list[0]
    for value in the_list:
        # replaces max with current value in list if it's greater
        if value > max:
            max = value
    index = 0  # tracks current index of list being compared to max
    while index < len(the_list):  # iterates through all indexes in list
        if the_list[index] == max:
            # removes all isntances of max
            the_list.pop(index)
            index -= 1  # since removing a value shifts all other values left
        index += 1
    return max
