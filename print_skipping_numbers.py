"""Examples of using break in Python loops."""


def easy() -> None:
    """Print numbers from 1 onward and stop at 8."""
    print("Easy (start at 1, stop at 8):")
    number = 1
    while True:
        print(number, end=" ")
        if number == 8:
            break
        number += 1
    print("\n")


def moderate() -> None:
    """Print 1..20 and stop when a multiple of 6 is found."""
    print("Moderate (1..20, stop at first multiple of 6):")
    for number in range(1, 21):
        print(number, end=" ")
        if number % 6 == 0:
            break
    print("\n")


def hard(target: int) -> None:
    """Search for target in 1..100 and stop when it is found."""
    print(f"Hard (search for {target} in range 1..100):")
    for number in range(1, 101):
        if number == target:
            print(f"Found {target} at {number}.")
            break
    else:
        print(f"{target} is not in the range 1..100.")


if __name__ == "__main__":
    easy()
    moderate()

    target_number = int(input("Enter a number to search (1..100): "))
    hard(target_number)
