"""A small Tkinter recipe book with local JSON storage."""

import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


# Locate the data beside the script, regardless of the working directory.
DATA_FILE = Path(__file__).resolve().with_name("recipes.json")


def load_recipes(path):
    """Read recipes and validate their required text fields.

    Args:
        path (Path): The JSON file to read.

    Returns:
        list: Recipe dictionaries, or an empty list for a missing file.

    Raises:
        OSError: If the file cannot be read.
        ValueError: If the file is not valid recipe data or UTF-8 text.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    recipes = json.loads(text)
    if not isinstance(recipes, list):
        raise ValueError("Recipe data must be a list.")
    for recipe in recipes:
        if not isinstance(recipe, dict) or any(
            not isinstance(recipe.get(field), str) or not recipe[field].strip()
            for field in ("title", "ingredients", "instructions")
        ):
            raise ValueError("Each recipe needs a title, ingredients, and instructions.")
    return recipes


def save_recipes(path, recipes):
    """Write a temporary file, then replace the previous collection.

    Args:
        path (Path): The destination JSON file.
        recipes (list): Recipe dictionaries containing text fields.

    Raises:
        OSError: If writing or replacing the file fails.
    """
    temporary_path = path.with_suffix(".tmp")
    temporary_path.write_text(
        json.dumps(recipes, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    # A failed write leaves the previous collection intact.
    temporary_path.replace(path)


class RecipeBook:
    """Group the recipe collection, editor, and button callbacks."""

    def __init__(self, root, recipes, path=DATA_FILE):
        """Build the recipe list and editor.

        Args:
            root (tk.Tk): The main application window.
            recipes (list): Previously loaded recipe dictionaries.
            path (Path): The file used for saving.
        """
        self.root = root
        self.recipes = recipes
        self.path = path
        self.selected_index = None
        root.title("Recipe Book")
        root.geometry("800x600")
        root.minsize(600, 450)
        root.protocol("WM_DELETE_WINDOW", self.close)

        sidebar = tk.Frame(root)
        sidebar.pack(side="left", fill="y", padx=10, pady=10)
        tk.Label(sidebar, text="Saved recipes").pack(anchor="w")
        self.recipe_list = tk.Listbox(sidebar, width=25, exportselection=False)
        self.recipe_list.pack(side="left", fill="y")
        scrollbar = tk.Scrollbar(sidebar, command=self.recipe_list.yview)
        scrollbar.pack(side="left", fill="y")
        self.recipe_list.config(yscrollcommand=scrollbar.set)
        self.recipe_list.bind("<<ListboxSelect>>", self.select_recipe)

        editor = tk.Frame(root)
        editor.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        tk.Label(editor, text="Title").pack(anchor="w")
        self.title = tk.Entry(editor)
        self.title.pack(fill="x")
        tk.Label(editor, text="Ingredients (one per line)").pack(anchor="w", pady=(10, 0))
        self.ingredients = ScrolledText(editor, height=7, wrap="word")
        self.ingredients.pack(fill="both", expand=True)
        tk.Label(editor, text="Instructions").pack(anchor="w", pady=(10, 0))
        self.instructions = ScrolledText(editor, height=10, wrap="word")
        self.instructions.pack(fill="both", expand=True)

        buttons = tk.Frame(editor)
        buttons.pack(fill="x", pady=10)
        tk.Button(buttons, text="New", command=self.new_recipe).pack(side="left")
        tk.Button(buttons, text="Save", command=self.save_recipe).pack(side="left", padx=5)
        tk.Button(buttons, text="Delete", command=self.delete_recipe).pack(side="left")
        self.status = tk.Label(editor, text="Enter a recipe, then click Save.", anchor="w")
        self.status.pack(fill="x")
        self.refresh_list()

    def read_form(self):
        """Read the editor with surrounding whitespace removed.

        Returns:
            dict: The title, ingredients, and instructions currently entered.
        """
        return {
            "title": self.title.get().strip(),
            "ingredients": self.ingredients.get("1.0", "end-1c").strip(),
            "instructions": self.instructions.get("1.0", "end-1c").strip(),
        }

    def can_discard(self):
        """Ask before leaving an editor with unsaved changes.

        Returns:
            bool: Whether navigation or closing may proceed.
        """
        current = self.read_form()
        if self.selected_index is None:
            changed = any(current.values())
        else:
            saved = self.recipes[self.selected_index]
            changed = any(current[key] != saved[key] for key in current)
        return not changed or messagebox.askyesno(
            "Unsaved changes", "Discard your unsaved changes?", parent=self.root
        )

    def refresh_list(self):
        """Rebuild the titles and restore the current selection."""
        self.recipe_list.delete(0, tk.END)
        for recipe in self.recipes:
            self.recipe_list.insert(tk.END, recipe["title"])
        if self.selected_index is not None:
            self.recipe_list.selection_set(self.selected_index)
            self.recipe_list.see(self.selected_index)

    def show_recipe(self):
        """Fill the editor with the selected recipe, or clear it for a new one."""
        recipe = (
            self.recipes[self.selected_index]
            if self.selected_index is not None
            else {"title": "", "ingredients": "", "instructions": ""}
        )
        self.title.delete(0, tk.END)
        self.title.insert(0, recipe["title"])
        for widget, field in (
            (self.ingredients, "ingredients"),
            (self.instructions, "instructions"),
        ):
            widget.delete("1.0", tk.END)
            widget.insert("1.0", recipe[field])

    def select_recipe(self, event=None):
        """Open a clicked recipe after checking for unsaved edits.

        Args:
            event (tk.Event or None): The optional list selection event.
        """
        selection = self.recipe_list.curselection()
        if not selection or selection[0] == self.selected_index:
            return
        if not self.can_discard():
            self.refresh_list()
            return
        self.selected_index = selection[0]
        self.show_recipe()
        self.status.config(text="Edit this recipe, then click Save.")

    def new_recipe(self):
        """Clear the editor after checking for unsaved edits."""
        if self.can_discard():
            self.selected_index = None
            self.refresh_list()
            self.show_recipe()
            self.title.focus_set()
            self.status.config(text="Enter a new recipe, then click Save.")

    def persist(self, recipes):
        """Write a proposed collection before updating the in-memory copy.

        Args:
            recipes (list): The proposed recipe collection.

        Returns:
            bool: Whether saving succeeded.
        """
        try:
            save_recipes(self.path, recipes)
        except OSError as error:
            messagebox.showerror(
                "Could not save", f"Your changes were not saved.\n\n{error}",
                parent=self.root,
            )
            return False
        self.recipes = recipes
        return True

    def save_recipe(self):
        """Validate the form and add or update one recipe."""
        recipe = self.read_form()
        if not all(recipe.values()):
            messagebox.showwarning(
                "Missing details", "Enter a title, ingredients, and instructions.",
                parent=self.root,
            )
            return
        updated = self.recipes.copy()
        index = self.selected_index
        if index is None:
            index = len(updated)
            updated.append(recipe)
        else:
            updated[index] = recipe
        if self.persist(updated):
            self.selected_index = index
            self.refresh_list()
            self.status.config(text="Recipe saved.")

    def delete_recipe(self):
        """Confirm deletion and save before removing the selected recipe."""
        if self.selected_index is None:
            messagebox.showinfo(
                "No recipe selected", "Select a saved recipe to delete.",
                parent=self.root,
            )
            return
        title = self.recipes[self.selected_index]["title"]
        if not messagebox.askyesno(
            "Delete recipe",
            f'Delete "{title}" and any unsaved edits to it?',
            parent=self.root,
        ):
            return
        updated = self.recipes.copy()
        del updated[self.selected_index]
        if self.persist(updated):
            self.selected_index = None
            self.refresh_list()
            self.show_recipe()
            self.status.config(text="Recipe deleted.")

    def close(self):
        """Close the window after checking for unsaved edits."""
        if self.can_discard():
            self.root.destroy()


def main():
    """Load the collection and start the GUI, or explain a loading error."""
    root = tk.Tk()
    root.withdraw()
    try:
        recipes = load_recipes(DATA_FILE)
    except (OSError, ValueError) as error:
        messagebox.showerror(
            "Could not load recipes",
            f"{DATA_FILE}\n\n{error}\n\n"
            "Back up and repair or rename this file, then restart the app.",
            parent=root,
        )
        # Do not open an empty editor that could overwrite an unreadable file.
        root.destroy()
        return
    RecipeBook(root, recipes)
    root.deiconify()
    root.mainloop()


if __name__ == "__main__":
    main()
