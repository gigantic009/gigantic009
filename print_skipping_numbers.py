"""Solutions for printing ranges while skipping specific multiples."""


def easy() -> None:
    """Print numbers 1..15 excluding multiples of 2."""
    print("Easy (1..15, skip multiples of 2):")
    for number in range(1, 16):
        if number % 2 == 0:
            continue
        print(number, end=" ")
    print("\n")


def moderate() -> None:
    """Print numbers 1..25 excluding multiples of 4."""
    print("Moderate (1..25, skip multiples of 4):")
    for number in range(1, 26):
        if number % 4 == 0:
            continue
        print(number, end=" ")
    print("\n")


def hard(n: int) -> None:
    """Print numbers 1..n excluding values divisible by 3 or 5."""
    print(f"Hard (1..{n}, skip numbers divisible by 3 or 5):")
    for number in range(1, n + 1):
        if number % 3 == 0 or number % 5 == 0:
            continue
        print(number, end=" ")
    print()


if __name__ == "__main__":
    easy()
    moderate()

    limit = int(input("Enter n for hard level: "))
    hard(limit)
