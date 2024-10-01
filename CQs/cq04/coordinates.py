"""Defines a function that takes 2 strs and prints the ordered pair combinations
for the characters in the strs"""


def get_coords(xs: str, ys: str) -> None:
    index_xs: int = 0  # tracks what index of xs is currently being paired
    # stops program when all indexes of xs have been iterated through
    while index_xs < len(xs):
        index_ys: int = 0  # tracks what index of should be printed
        # exits loop once all indexes of ys have been iterated through
        while index_ys < len(ys):
            print("(" + xs[index_xs] + "," + ys[index_ys] + ")")
            index_ys += 1  # adds to index of ys to be printed next
        index_xs += 1  # adds to index of xs to be printed next
