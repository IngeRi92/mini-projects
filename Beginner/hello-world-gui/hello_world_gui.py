import tkinter as tk
import random


# Klass võimaldab meil luua objekti, mis sisaldab kogu rakenduse loogikat ja GUI komponente.


class HelloWorldApp:
    def __init__(self):
        self.window = tk.Tk()  # Loome Tkinteri akna objekti
        self.window.title("Hello World GUI")
        self.window.geometry("400x300")

        # .pack() on meetod, mis paigutab GUI komponendid aknas vertikaalselt üksteise alla.
        tk.Label(self.window, text="Hello World App", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.window, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        # command seob nupu vajutuse funktsiooniga.
        tk.Button(self.window, text="Say Hello", command=self.say_hello).pack(pady=5)
        tk.Button(
            self.window, text="Random Greeting", command=self.random_greeting
        ).pack(pady=5)

        self.message_label = tk.Label(
            self.window,
            text="Welcome! Enter your name and click a button.",
            wraplength=350,
        )
        self.message_label.pack(pady=10)

    def say_hello(self):
        name = self.name_entry.get().strip()
        if name:
            message = f"Hello, {name}! Nice to meet you!"
        else:
            message = "Hello, World! Please enter your name for a personal greeting."
        self.message_label.config(text=message)

    def random_greeting(self):
        name = self.name_entry.get().strip()
        greetings = [
            "Greetings",
            "Welcome",
            "Good day",
            "Howdy",
            "Hello there",  # General Kenobi
            "Salutations",
        ]
        greeting = random.choice(greetings)
        if name:
            message = f"{greeting}, {name}! Hope you're having a great day!"
        else:
            message = f"{greeting}! Enter your name for a personal touch."
        self.message_label.config(text=message)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = HelloWorldApp()
    app.run()
