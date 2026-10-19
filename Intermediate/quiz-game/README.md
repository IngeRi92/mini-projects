# Quiz Game with GUI

A simple multiple-choice quiz about Python basics, built with Tkinter.
All the code and questions live in one file so they are easy to explore.

## Features

- Answer five questions using buttons
- See whether your answer is correct and learn the correct answer
- Read feedback before moving to the next question
- Count each question only once and show the final score
- Play again without reopening the window
- Use Python's standard library with no pip packages

## How to Run

1. Make sure you have Python 3 with Tkinter installed and a desktop display.
   Tkinter is included with most Python installations. If importing
   `tkinter` fails, install Tk support for your Python distribution.
2. From the project root, run:

   ```bash
   python Intermediate/quiz-game/quiz_game.py
   ```

   Or, from this folder, run `python quiz_game.py`.

3. Click an answer. The answer buttons become disabled so you cannot
   change the answer or earn extra points on the same question.
4. Read the feedback, then click **Next**. After the last question,
   **Next** shows your score.
5. Click **Play Again** to reset the quiz, or close the window to exit.

## Example

```text
Question 1 of 5
Which function displays text in Python?

[input()]
[print()]
[len()]

Choose an answer.
[Next] (disabled until you answer)
```

Choosing `print()` shows `Correct!` and enables **Next**. Each correct
answer earns one point; incorrect answers earn no points. Answering all
five correctly ends with `Your score: 5/5`.

## How the Code Works

1. `QUESTIONS` is a list of dictionaries. Each dictionary has a
   `question`, a list of `choices`, and an `answer` matching one choice.
2. `QuizGame` is a class that groups the interface and quiz state.
   `self` refers to the current game object. Attributes such as
   `self.score` keep values available across button clicks.
3. `__init__()` creates labels, a frame to hold answer buttons, and a
   **Next** button. `pack()` places widgets in the window.
4. `restart()` resets the score and question index. Python lists start
   at index `0`, so the progress label adds `1` for the player.
5. `show_question()` creates the choice buttons and disables **Next**
   until an answer is selected. `lambda answer=choice: ...` creates a
   small callback that remembers the choice belonging to each button.
6. `check_answer()` compares the selected answer with the stored answer,
   updates the score and feedback, and prevents repeat answers.
7. `next_question()` advances through the list. At the end, it shows the
   score and changes the **Next** button into **Play Again**.
8. `main()` creates the window. `mainloop()` listens for events such as
   button clicks and runs their callbacks. Passing `command=self.restart`
   gives Tkinter a function to call later; adding `()` would call it now.

The `if __name__ == "__main__":` block starts the app when run directly,
while allowing imports without opening a window.

## Customize the Questions

Edit `QUESTIONS` in `quiz_game.py`. Keep at least one question, give each
question nonempty, distinct choices, and copy the correct choice exactly
into `answer`. For example, add this dictionary inside the list:

```python
{
    "question": "What is 2 ** 3?",
    "choices": ["5", "6", "8"],
    "answer": "8",
},
```

The progress and final score automatically use the number of questions.
Questions appear in the same order each round; scores are not saved.

## Ideas to Try Next

- Add your own questions
- Shuffle the question order each round
- Save the highest score to a text file

---

Project for learning purposes.
