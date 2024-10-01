"""wordle game"""

__author__ = "730742450"


def input_guess(num_characters: int) -> str:
    """Asks user to enter string until it meets char length specified"""
    # takes initial input
    guess: str = input(f"Enter a {num_characters} character word: ")
    while len(guess) != num_characters:
        # continues taking inputs until input length = num_characters
        guess = input(f"That wasn't {num_characters} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if any index of secret_word matches char_guess"""
    # ensures length of character is 1, otherwise error
    assert len(char_guess) == 1
    index: int = 0  # tracks index of secret_word currently being compared
    while index < len(secret_word):  # iterates through all indexes of secret_word
        if secret_word[index] == char_guess:  # returns true if a match is found
            return True
        index += 1  # adds 1 to index of secret_word currently being compared
    return False  # returns false if no match found between secret_word and char_guess


def emojified(guess: str, secret_word: str) -> str:
    """returns a str composed of colored boxes signifying whether
    characters in guess are in the correct position, present, or not present"""
    # ensures length of guess = length of secret word
    assert len(guess) == len(secret_word)
    # named constants for colored boxes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojified_guess: str = ""
    index_guess: int = 0  # tracks index of guess being compared
    while index_guess < len(guess):  # iterates through every index of guess
        # checks if index of guess is in the correct position
        if guess[index_guess] == secret_word[index_guess]:
            emojified_guess += GREEN_BOX
        # checks if index of guess is present in secret word
        elif contains_char(secret_word, guess[index_guess]):
            emojified_guess += YELLOW_BOX
        # adds white box to emojified guess if index of guess not present
        else:
            emojified_guess += WHITE_BOX
        index_guess += 1  # adds 1 to index of guess being analyzed
    return emojified_guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # state of game is defined below
    turn: int = 1
    GREEN_BOX: str = "\U0001F7E9"
    while turn <= 6:  # runs game for 6 turns
        print(f"=== Turn {turn}/6 ===")  # prints current turn number
        # gathers guess from user that is the same length as secret word
        guess = input_guess(len(secret))
        print(emojified(guess, secret))  # prints emojified guess
        if emojified(guess, secret) == GREEN_BOX * len(secret):  # checks if user won
            print(f"You won in {turn}/6 turns!")
            # quits program is user wins
            return None
        turn += 1  # adds 1 to current turn
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    # makes it possible to run program as module or import functions into other modules
    main(secret="codes")
