# Number Guessing Game

A simple command-line guessing game where the player tries to guess a randomly generated number between 1 and 100.

## Features

- Random number generation between 1-100
- 7 attempts to guess the correct number
- Input validation for user entries
- Helpful hints (too high/too low)
- Play again functionality
- Clean, professional interface

## How to Run

1. Save the code as `number_guessing_game.py`
2. Run in terminal:

```bash
python number_guessing_game.py
```

## Example Gameplay

```
Welcome to Number Guessing Game!
I'm thinking of a number between 1 and 100.

Attempt 1/7 - Enter your guess: 50
Too high! Try a lower number.
You have 6 attempts remaining.

Attempt 2/7 - Enter your guess: 25
Too low! Try a higher number.
You have 5 attempts remaining.

Attempt 3/7 - Enter your guess: 37
Congratulations! You guessed the number 37 in 3 attempts!

Do you want to play again? (y/n): n
Thanks for playing!
```

## Technical Details

**Core Functions:**

- `random.randint(1, 100)` - Generates random number
- Input validation with try/except
- While loop for game logic
- Recursive function call for replay

**Game Rules:**

- Player has 7 attempts maximum
- Numbers range from 1 to 100
- Hints provided after each guess
- Option to replay after game ends

## Learning Objectives

This project demonstrates:

- Random number generation
- User input and validation
- Control flow (loops and conditionals)
- Exception handling
- Function organization
- Recursion (play again feature)

## Requirements

- Python 3.x
- No external dependencies
