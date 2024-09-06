"""mimic program"""

__author__ = "730742450"


def mimic(message: str) -> str:
    """repeats the message passed as an argument"""
    return message


def main() -> None:
    """Main function; prints the return value of mimic given a specified argument."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
