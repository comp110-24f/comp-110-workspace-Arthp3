"""pytest file for utils.py"""

__author__ = "730742450"

from utils import only_evens, sub, add_at_index
import pytest

"""only_evens tests"""


def test_only_evens_return() -> None:
    """tests that only_evens returns correctly"""
    assert only_evens([1, 2, 2, 8, 7, 34]) == [2, 2, 8, 34]


def test_only_evens_mutate() -> None:
    """tests that only_evens does NOT mutate the inputted list"""
    old_list: list[int] = [1, 2, 2, 8, 7, 34]
    only_evens(old_list)
    assert old_list == [1, 2, 2, 8, 7, 34]


def test_only_evens_edge() -> None:
    """tests only_evens edge case (if inputted list is fully odd)"""
    assert only_evens([1, 7, 15, 9]) == []


"""sub tests"""


def test_sub_return() -> None:
    """tests that sub returns correctly"""
    assert sub([25, 14, 36, 4, 8, 12], 1, 4) == [14, 36, 4]


def test_sub_mutate() -> None:
    """tests that sub does NOT mutate the inputtd list"""
    the_list: list[int] = [25, 14, 36, 4, 8, 12]
    sub([25, 14, 36, 4, 8, 12], 1, 4)
    assert the_list == [25, 14, 36, 4, 8, 12]


def test_sub_edge() -> None:
    """tests that sub returns correctly with out of bound start and end index"""
    assert sub([25, 14, 36, 4, 8, 12], start=-2, end=500) == [25, 14, 36, 4, 8, 12]


"""add_at_index tests"""


def test_add_at_index_return() -> None:
    """tests add_at_index returns None"""
    assert add_at_index([18, 4, 37, 12], element=44, input_index=2) is None


def test_add_at_index_mutate() -> None:
    """tests that add_at_index mutates list correctly"""
    the_list: list[int] = [18, 4, 37, 12]
    add_at_index(the_list, element=44, input_index=2)
    assert the_list == [18, 4, 44, 37, 12]


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    the_list: list[int] = [1, 2, 3, 4, 5]
    with pytest.raises(IndexError):
        # an IndexError is raised whn specified index is below 0
        add_at_index(the_list, 26, -4)
    with pytest.raises(IndexError):
        # an IndexError is raised when specified index is greater than list length
        add_at_index(the_list, 26, 5)
