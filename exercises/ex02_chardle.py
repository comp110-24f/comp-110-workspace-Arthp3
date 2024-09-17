"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730742450"


def input_word() -> str:
    """Asks for 5-character word, provides feedback on if word meets requirements"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Asks for character, provides feedback on if it meets requirement"""
    character: str = input("Enter a single character: ")
    if len(character) != 1:
        print("Error: Character must be a single character.")
        exit()
    return character


def contains_char(word: str, letter: str) -> None:
    """Counts instances of character in word"""
    print("Searching for " + letter + " in " + word)

    count: int = 0
    index: int = 0

    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count = count + 1
        index = index + 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Runs Chardle game"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
