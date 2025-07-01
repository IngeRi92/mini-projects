import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root  # root-tkinteri akna loomine= main_window, pythoni standard
        self.root.title("To-Do List")
        self.tasks = []

        # GUI elemendid
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(
            root, text="Remove Task", command=self.remove_task
        )
        self.remove_button.pack(pady=5)

        self.load_tasks()  # Laadib salvestatud ülesanded

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)
            self.tasks.pop(selected[0])
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as f:  # f = fail
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()  # tkinteri akna tsükkel, mis hoiab akna avatuna
    # Kui see eemaldada, siis programm lõpetab töö kohe
