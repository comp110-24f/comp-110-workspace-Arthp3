"""Summing the elements of a list using different loops"""

__author__ = "730742450"


def w_sum(vals: list[float]) -> float:
    """returns sum of floats in list using while loop"""
    index = 0
    sum = 0
    while index < len(vals):  # repeats for length of list
        sum += vals[index]  # adds current index value to sum
    return sum


def f_sums(vals: list[float]) -> float:
    """returns sum of floats in list using for loop"""
    sum = 0
    for value in vals:
        sum += value  # adds current value in list to sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    """returns sum of floats in list using for ... in range () loop"""
    sum = 0
    for index in range(0, len(vals)):
        sum += vals[index]  # adds current index value to sum
    return sum
