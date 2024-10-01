"""Counts instances of a letter in a word"""

__author__: str = "730742450"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # Tracks instances of search_char found in phrase
    index: int = 0  # Tracks current index of phrase being compared to search_char

    while index < len(phrase):
        # Adds 1 to count if search_char matches current index of phrase
        if search_char == phrase[index]:
            count = count + 1
        index = index + 1  # Adds 1 to index of phrase that will be compared to

    return count  # Returns count of search_char found in phrase
