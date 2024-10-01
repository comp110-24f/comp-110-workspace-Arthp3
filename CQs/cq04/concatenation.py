"""defines 2 str variables and concatenates them together using a function"""


def concat(str1: str, str2: str) -> str:
    # concatenates 2 words
    return str1 + str2


if __name__ == "__main__":
    # does not run the following code when module is imported
    word1: str = "happy"  # assigns "happy" to variable word1
    word2: str = "tuesday"  # assigns "tuesday to variable word2"
    print(concat(word1, word2))  # prints the concatenation of word1 and word2
