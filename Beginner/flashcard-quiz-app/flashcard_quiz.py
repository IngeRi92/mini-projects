"""A simple command-line flashcard quiz for practicing Python basics."""


def play_quiz(flashcards):
    """Ask each flashcard question and show feedback after each answer.

    Answers ignore capital letters and spaces at the start and end.
    An empty answer counts as incorrect and reveals the correct answer.

    Args:
        flashcards (list[dict]): Cards with 'question' and 'answer' keys.

    Returns:
        int: The number of correct answers.
    """
    # Start each new quiz with zero points.
    score = 0

    for card in flashcards:
        print(f"\n{card['question']}")
        user_answer = input("Your answer: ").strip().lower()

        # Compare both answers in lowercase so 'PRINT' also matches 'print'.
        if user_answer == card["answer"].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"The correct answer is: {card['answer']}")

    return score


def main():
    """Run the flashcard quiz and repeat when the player enters 'y' or 'yes'.

    Show the total score after each quiz. Any other replay response
    ends the program.

    Returns:
        None.
    """
    # Each dictionary holds one question and its answer.
    # Add more dictionaries to this list to create your own flashcards.
    flashcards = [
        {"question": "Which function displays text? (name only)", "answer": "print"},
        {"question": "Which function reads user input? (name only)", "answer": "input"},
        {"question": "Which keyword starts a function definition?", "answer": "def"},
        {"question": "Which symbol starts a comment?", "answer": "#"},
        {"question": "What is the result of 3 * 4?", "answer": "12"},
    ]

    print("Welcome to Flashcard Quiz App!")
    print("Practice Python basics. Press Enter to reveal an answer if you are stuck.")

    while True:
        score = play_quiz(flashcards)
        print(f"\nYour score: {score}/{len(flashcards)}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            break

    print("Thanks for practicing!")


# Start the app only when this file is run directly.
if __name__ == "__main__":
    main()
