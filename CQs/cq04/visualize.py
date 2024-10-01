"""Defines 2 vars x and y and prints their concatenation
and coordinate pairsw for their characters"""

from concatenation import concat  # imports concat function
from coordinates import get_coords  # inports get_coords function

x: str = "123"  # defines var x as "123"
y: str = "abc"  # defines var y as "abc"

print(concat(x, y))  # pritns the concatenation of x and y
get_coords(x, y)
