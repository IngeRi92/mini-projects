# Guess the Word Game

A simple command-line game in Python where you guess a word from a clue.
The Python file stays under 100 lines, including docstrings and blank lines.

## Features

- Guess a randomly chosen word using a clue and its length
- Get five attempts to guess the whole word
- Accepts uppercase or lowercase guesses and ignores surrounding spaces
- Blank input, nonletters, and repeated guesses do not use attempts
- Reveals the answer when you win or run out of attempts
- Play again without restarting the program

## How to Run

1. Make sure you have Python 3 installed. No extra packages are needed.
2. From the project root, run:

   ```bash
   python Beginner/guess-the-word-game/guess_the_word.py
   ```

   Or, from this folder, run `python guess_the_word.py`.

## Example

```text
Welcome to Guess the Word!
Use the clue to guess the whole word in five attempts.

Clue: A large body of salt water.
The word has 5 letters.
Your guess (5 attempts left): river
Not quite. Try again!
Your guess (4 attempts left): ocean
You win! The word was 'ocean'.

Play again? (y/n): n
Thanks for playing!
```

Words are chosen randomly, so the clue may change each round. The same word
can appear again. Enter `y` or `yes` to play again; any other response exits.

## How the Code Works

- `WORDS` stores pairs of words and clues in a list of tuples.
- `play_round()` uses a loop, conditions, and a list of previous guesses to
  check input and track the remaining attempts.
- `strip()` removes surrounding spaces, and `lower()` makes guesses
  case-insensitive. `isalpha()` checks that the guess contains only letters.
- `main()` picks a pair with `random.choice()` and handles replay.
- The `if __name__ == "__main__":` guard starts the game when the file is
  run directly, but not when it is imported.

To add more words, add a lowercase word and its clue to `WORDS`, following
the existing pairs. Use words containing only letters, without spaces.

---

Project for learning purposes.
