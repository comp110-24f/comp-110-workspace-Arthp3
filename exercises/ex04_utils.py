"""defines 'all', 'max', 'is_equal', and 'extend' functions for mutating lists"""

__author__ = "730742450"


def all(the_list: list[int], the_int: int) -> bool:
    """indicates whether all ints in the list as the same as the_int"""
    if(len(the_list)) == 0 #returns false if length of list is 0
        return False
    for index in the_list:  # repeats the following for every index in the list
        if index != the_int:
            return False  # returns False if any index in list doesn't match the_int
    return True  # returns True if all indexes in list match the_int


def max(the_list: list[int]) -> int:
    """returns greatest value in the list"""
    max = the_list[0]  # initializes max as the first value in the list
    if len(the_list) == 0:
        raise ValueError("max() arg is an empty List")
    for index in the_list:  # repeats the following for every index in the list
        if index > max:
            max = index  # replaces max with current value if it's > previous max
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """returns true if every corresponding element in lists is equal"""
    index = 0
    while index < len(list1):
        if (list1[index] != list2[index]):  
            # returns false if the values at current index in both lists don't match
            return False
        index +=1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """appends the whole second list to the end of the first list"""
    for i in list2:
        list1.append(i)  # appends current value in list2 to end of list1
