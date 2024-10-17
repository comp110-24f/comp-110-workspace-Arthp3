"""contains only_evens, sub, and add_at_index functions for lists"""

__author__ = "730742450"


def only_evens(the_list: list[int]) -> list[int]:
    """returns a list with only evens from inputted list"""
    new_list: list[int] = []
    for value in the_list:
        if value % 2 == 0:  # tests for even value
            new_list.append(value)
    return new_list


def sub(the_list: list[int], start: int, end: int) -> list[int]:
    """creates a subset list between the specified start and end index"""
    if start < 0:
        # addresses a negative starting index by changing it to 0
        index: int = 0
    else:
        index: int = start
    new_list: list[int] = []
    # Repeats until specified end index or end of the_list reached
    while (index < end) and (index < len(the_list)):
        new_list.append(the_list[index])  # adds all values in range to the next list
        index += 1
    return new_list


def add_at_index(the_list: list[int], element: int, input_index: int) -> None:
    """adds specified element to specified index in list"""
    if input_index < 0 or input_index > len(the_list):
        # ensures the specified index is within range
        raise IndexError("Index is out of bounds for the input list")
    the_list.append(0)  # lengthens list by 1 (to make space for new element)
    index: int = len(the_list) - 1  # starts at the end of the list
    while index >= input_index:  # loops until the specified input_index is reached
        the_list[index] = the_list[index - 1]  # assigns value of previous index to next
        index -= 1
    the_list[input_index] = element  # assigns element to specified input_index
