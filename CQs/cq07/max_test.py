"""pytests file for find_max"""

__author__ = "730742450"

from find_max import find_and_remove_max


def test_return() -> None:
    """ensures find_and_remove_max returns the expected value"""
    assert find_and_remove_max([1, 50, 14, 8]) == 50


def test_mutate() -> None:
    """ensures find_and_remove_max mutates the input in the expected way"""
    the_list = [1, 50, 14, 8, 50]
    find_and_remove_max(the_list)
    assert the_list == [1, 14, 8]
    the_list = [1, 8, 2, 3, 3]
    find_and_remove_max(the_list)
    assert the_list == [1, 2, 3, 3]


def test_edge() -> None:
    """ensures correct reutnr in case of an unconventional input"""
    assert find_and_remove_max([]) == -1  # tests function for an empty list
