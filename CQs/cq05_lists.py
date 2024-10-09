"""Mutating functions."""

__author__: str = "730742450"


def manual_append(the_list: list[int], the_int: int) -> None:
    """Appends the int to the end of the list"""
    the_list.append(the_int)


def double(the_list: list[int]) -> None:
    """Doubles the value of each index in the list"""
    index: int = 0
    while index < len(the_list):  # repeats for each index in the list
        the_list[index] = the_list[index] * 2  # multiplies current index value by 2
        index += 1


# initializes 2 variables poijnting to the same object(list)
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

# doubles tbe value of each index in list_2
double(list_2)
# prints list_1 and list_2
print(list_1)
print(list_2)
