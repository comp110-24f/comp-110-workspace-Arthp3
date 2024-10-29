"""holds functions related to dictionaries"""

__author__ = "730742450"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """inverts keys and values in dictionary"""
    inverted: dict[str, str] = {}
    values: list[str] = []
    for key in dictionary:
        # sees if this value already appeared in dictionary
        if dictionary[key] in values:
            raise KeyError("error message of your choice here!")
        values.append(dictionary[key])
    for key in dictionary:
        # flips placement of keys and values
        inverted[dictionary[key]] = key
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns most repeated color in dictionary"""
    colors: dict[str, int] = {}

    # Count repetitions of each color
    for name in dictionary:
        if dictionary[name] in colors:
            colors[dictionary[name]] += 1
        else:
            colors[dictionary[name]] = 1

    # current highest repetition count and popular color
    popular = ""
    highest = 0
    # Find the most popular color
    for color in colors:
        if colors[color] > highest:
            popular = color
            highest = colors[color]

    return popular


def count(the_list: list[str]) -> dict[str, int]:
    # returns dictionary containing cvalues in list and their count
    dictionary: dict[str, int] = {}
    for item in the_list:
        if item in dictionary:
            # If item is in dictionary, adds 1 to its value
            dictionary[item] += 1
        else:
            # Else adds the item as a key with a value of 1
            dictionary[item] = 1
    return dictionary


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Given a list[str], returns a dict[str, list[str]] where each key is a letter and
    each value is a list of words beginning with that letter"""
    dictionary: dict[str, list[str]] = {}
    for word in words:
        # sees if first letter of each word already in dictionary
        if word[0].lower() in dictionary:
            # if so, appends that word to the value of that key in the dictionary
            dictionary[word[0].lower()].append(word)
        else:
            # else, creates a key in dictionary for the first letter of the word
            dictionary[word[0].lower()] = [word]
    return dictionary


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """adds a student to the list of attendance for a day of the week"""
    if day in attendance:
        if not (student in attendance[day]):
            # If day is in dictionary but student isn't, append student's name to value
            attendance[day].append(student)
    else:
        # Else, create a new key for the day
        attendance[day] = [student]
