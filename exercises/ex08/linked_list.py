"""Functions for dealing with linked lists."""

from __future__ import annotations


class Node:
    """Defines the Node class."""
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Constructor for Node objects."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Intended string return for Node objects."""
        rest: str = ""
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def recursive_range(start: int, end: int) -> Node | None:
    """Creates linked list with values from start to end."""
    # Edge case
    if start > end:
        raise ValueError("Start cannot be greater than end.")
    # Base case
    if start == end:
        return None
    # Recursive case
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)    


print(recursive_range(1, 1))
print(recursive_range(1, 5))
my_node: Node | None = Node(110, Node(111, Node(112, None)))
print(my_node)


def last(head: Node) -> int:
    """Returns value of previous Node."""
    if head.next is None: 
        return head.value
    else:
        return last(head.next)    


two: Node = Node(2, None)
one: Node = Node(1, two)
print(one)
print(last(one))


def value_at(head: Node | None, index: int) -> int:
    """Return the data of the Node stored at the given index."""
    # Edge case
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Base case
    if index == 0:
        return head.value
    # Recursive case
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum data value in the linked list."""
    # Edge case
    if head is None:
        raise ValueError("Cannot call max with None")
    # Base Case
    if head.next is None: 
        return head.value
    # Recursive Case
    current_max: int = max(head.next)
    if head.value > current_max:
        return head.value
    else:
        return current_max


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values, in the same order, as the input list."""
    # Base case
    if len(items) == 0:
        return None
    # Recursive case
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
    # Base case
    if head is None:
        return None
    # Recursive case
    return Node(head.value * factor, scale(head.next, factor))