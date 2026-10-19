"""A simple multiple-choice Python quiz using Tkinter."""

import tkinter as tk


# Each dictionary stores one question, its choices, and the correct choice.
QUESTIONS = [
    {
        "question": "Which function displays text in Python?",
        "choices": ["input()", "print()", "len()"],
        "answer": "print()",
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "choices": ["//", "#", "!"],
        "answer": "#",
    },
    {
        "question": "What does len('cat') return?",
        "choices": ["2", "3", "4"],
        "answer": "3",
    },
    {
        "question": "Which type stores True or False?",
        "choices": ["str", "int", "bool"],
        "answer": "bool",
    },
    {
        "question": "Which keyword defines a function?",
        "choices": ["def", "for", "if"],
        "answer": "def",
    },
]


class QuizGame:
    """Keep the quiz's widgets, current question, and score together."""

    def __init__(self, root):
        """Build the interface and start the first round.

        Args:
            root (tk.Tk): The main application window.
        """
        root.title("Quiz Game")

        self.progress_label = tk.Label(root)
        self.progress_label.pack(padx=20, pady=10)

        self.question_label = tk.Label(root, wraplength=400, font=("Arial", 14))
        self.question_label.pack(padx=20, pady=10)

        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack(fill="x", padx=20)

        self.feedback_label = tk.Label(root, wraplength=400)
        self.feedback_label.pack(padx=20, pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(padx=20, pady=10)

        self.restart()

    def restart(self):
        """Reset the score and show the first question.

        Returns:
            None.
        """
        self.question_index = 0
        self.score = 0
        self.next_button.config(text="Next", command=self.next_question)
        self.show_question()

    def show_question(self):
        """Display the current question with a button for each choice.

        Returns:
            None.
        """
        # Remove the previous question's buttons before creating new ones.
        for button in self.choices_frame.winfo_children():
            button.destroy()

        question = QUESTIONS[self.question_index]
        self.progress_label.config(
            text=f"Question {self.question_index + 1} of {len(QUESTIONS)}"
        )
        self.question_label.config(text=question["question"])
        self.feedback_label.config(text="Choose an answer.")
        self.next_button.config(state="disabled")
        self.answered = False

        for choice in question["choices"]:
            # The default argument remembers this loop iteration's choice.
            button = tk.Button(
                self.choices_frame,
                text=choice,
                command=lambda answer=choice: self.check_answer(answer),
            )
            button.pack(fill="x", pady=3)

    def check_answer(self, answer):
        """Check one answer and allow the player to continue.

        Args:
            answer (str): The text of the selected choice.

        Returns:
            None.
        """
        # Count only the first answer, even if the player clicks again.
        if self.answered:
            return
        self.answered = True
        correct_answer = QUESTIONS[self.question_index]["answer"]
        if answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!")
        else:
            self.feedback_label.config(text=f"Correct answer: {correct_answer}")

        for button in self.choices_frame.winfo_children():
            button.config(state="disabled")
        self.next_button.config(state="normal")

    def next_question(self):
        """Move to the next question or display the final score.

        Returns:
            None.
        """
        self.question_index += 1
        if self.question_index < len(QUESTIONS):
            self.show_question()
        else:
            for button in self.choices_frame.winfo_children():
                button.destroy()
            self.progress_label.config(text="Quiz complete!")
            self.question_label.config(text=f"Your score: {self.score}/{len(QUESTIONS)}")
            self.feedback_label.config(text="Play again to practice.")
            self.next_button.config(text="Play Again", command=self.restart)


def main():
    """Create the window and listen for button clicks until it closes.

    Returns:
        None.
    """
    root = tk.Tk()
    QuizGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
