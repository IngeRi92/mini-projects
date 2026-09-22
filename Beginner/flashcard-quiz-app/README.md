# Flashcard Quiz App

A simple command-line quiz for practicing Python basics.

## Features

- Answer five built-in flashcards, one at a time
- Get feedback and see the correct answer after a mistake
- Press Enter to reveal an answer (no point is awarded)
- Answers ignore capital letters and spaces at the start and end
- See your total score and play again

## How to Run

1. Make sure you have Python 3 installed. No extra packages are needed.
2. From the project root, run:

   ```bash
   python Beginner/flashcard-quiz-app/flashcard_quiz.py
   ```

   Or, from this folder, run `python flashcard_quiz.py`.

## Example

```text
Welcome to Flashcard Quiz App!
Practice Python basics. Press Enter to reveal an answer if you are stuck.

Which function displays text? (name only)
Your answer: PRINT
Correct!

Which function reads user input? (name only)
Your answer: print
The correct answer is: input
```

After all five cards, the app shows your score. Enter `y` or `yes` to
play again with a fresh score; any other response ends the program.

## Change the Flashcards

Edit the `flashcards` list inside `main()` in `flashcard_quiz.py`.
Each dictionary contains a question and a single expected answer:

```python
{"question": "What is the result of 2 + 2?", "answer": "4"},
```

Keep both values as strings (inside quotes). Cards appear in the order
they are listed. Changes to the list are used the next time you run the app.

## What You Practice

- Lists and dictionaries to store flashcards
- `input()` and `print()` to interact with the player
- Loops and `if`/`else` to check answers
- String methods to clean up input
- Functions and a variable to keep score

---

Project for learning purposes.
