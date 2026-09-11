"""A command-line app for rolling six-sided dice and displaying their total."""

import random


def get_dice_count():
    """Ask how many dice to roll, retrying until the input is valid.

    Pressing Enter without a number selects one die.

    Returns:
        int: The selected number of dice, between 1 and 10 inclusive.
    """
    while True:
        user_input = input("How many dice? (1-10, default: 1): ").strip()
        if not user_input:
            return 1
        try:
            count = int(user_input)
            if 1 <= count <= 10:
                return count
        except ValueError:
            pass
        print("Please enter a whole number between 1 and 10.")


def roll_dice(count):
    """Generate a random result for each six-sided die.

    Args:
        count (int): Number of dice to roll. The caller is expected to
            provide a value between 1 and 10; this function does not
            validate that range.

    Returns:
        list[int]: One random number between 1 and 6 inclusive per die.
    """
    return [random.randint(1, 6) for _ in range(count)]


def main():
    """Run the interactive dice roller.

    Ask for a dice count, display individual results and their total,
    and repeat when the user enters 'y' or 'yes' (case-insensitive).
    Any other response ends the program.

    Returns:
        None.
    """
    print("Welcome to Dice Roller!")
    print("Roll up to 10 six-sided dice at a time.")

    while True:
        count = get_dice_count()
        results = roll_dice(count)
        print()
        for number, result in enumerate(results, start=1):
            print(f"Die {number}: {result}")
        print(f"Total: {sum(results)}")

        if input("\nRoll again? (y/n): ").lower().strip() not in ["y", "yes"]:
            break
        print()

    print("Thanks for rolling!")


if __name__ == "__main__":
    main()
