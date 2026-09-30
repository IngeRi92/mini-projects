"""A command-line game where players guess a word from a clue."""

import random


WORDS = [
    ("python", "A programming language named after a comedy group."),
    ("keyboard", "You use this to type on a computer."),
    ("ocean", "A large body of salt water."),
    ("guitar", "A musical instrument with six strings."),
    ("rainbow", "A colorful arc that can appear after rain."),
]


def play_round(word, clue):
    """Give the player five attempts to guess a secret word.

    Blank input, nonletters, and repeated guesses do not use attempts.

    Args:
        word (str): The lowercase secret word containing only letters.
        clue (str): A hint to help the player guess the word.

    Returns:
        None.
    """
    attempts = 5
    guesses = []
    print(f"\nClue: {clue}")
    print(f"The word has {len(word)} letters.")

    while attempts > 0:
        guess = input(f"Your guess ({attempts} attempts left): ").strip().lower()
        if not guess.isalpha():
            print("Please enter a word using letters only.")
            continue
        if guess in guesses:
            print("You already tried that word. Try another one.")
            continue

        guesses.append(guess)
        if guess == word:
            print(f"You win! The word was '{word}'.")
            return

        attempts -= 1
        if attempts > 0:
            print("Not quite. Try again!")

    print(f"Out of attempts! The word was '{word}'.")


def main():
    """Choose random words and repeat when the player enters 'y' or 'yes'.

    Any other replay response ends the program.

    Returns:
        None.
    """
    print("Welcome to Guess the Word!")
    print("Use the clue to guess the whole word in five attempts.")

    while True:
        word, clue = random.choice(WORDS)
        play_round(word, clue)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
