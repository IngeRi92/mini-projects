# Recipe Book App

A simple desktop recipe book built with Tkinter. Keep your recipes in a
local JSON file, with all the Python code in one file.
The included `recipes.json` contains an example recipe for **Ühepajatoit**
(Estonian meat and vegetable stew), written in Estonian.

## Features

- Add recipes with a title, ingredients, and instructions
- Select a saved recipe to view or edit it
- Delete recipes after confirmation
- Save recipes between sessions using JSON
- Explore an included example recipe
- Check for blank fields and warn before discarding unsaved edits
- Use Python's standard library with no pip packages

## How to Run

1. Make sure you have Python 3 with Tkinter installed and a desktop display.
   Tkinter is included with most Python installations. If importing
   `tkinter` fails, install Tk support for your Python distribution.
2. From the project root, run:

   ```bash
   python Intermediate/recipe-book-app/recipe_book.py
   ```

   Or, from this folder, run `python recipe_book.py`.

3. Select **Ühepajatoit** on the left to view the included example.
   To add your own recipe, click **New**, then enter a title, ingredients
   (one per line), and cooking instructions.
   Click **Save** to add the recipe.
4. Select a title on the left to view it. Change any fields and click
   **Save** to update that recipe.
5. Click **New** to start another recipe, or **Delete** to remove the
   selected recipe after confirmation.

## Example

```text
Title: Tomato Toast

Ingredients:
1 slice of bread
1 tomato
1 teaspoon olive oil

Instructions:
1. Toast the bread.
2. Slice the tomato and place it on the toast.
3. Drizzle with olive oil and serve.
```

Click **Save** and `Tomato Toast` appears in the list. Close and reopen
the app to find the recipe still there. Editing a selected recipe updates
that entry; use **New** when you want to add a separate recipe.

## How the Code Works

1. `DATA_FILE` uses `Path(__file__)` to locate `recipes.json` next to the
   script, regardless of the directory you launch it from.
2. `load_recipes()` reads JSON into a list of dictionaries and validates
   the required text fields. A missing file starts an empty collection.
3. `RecipeBook` groups the widgets and state. `selected_index` is the
   position of the selected recipe, or `None` when creating a new one.
4. `read_form()` collects text from the widgets. `save_recipe()` rejects
   blank fields and builds an updated copy of the recipe list.
5. `persist()` calls `save_recipes()` before changing the in-memory list.
   The data is written to a temporary file, which then replaces the old
   file. If saving fails, the app displays an error and keeps the editor.
6. `refresh_list()` displays recipe titles. `select_recipe()` and
   `show_recipe()` load the chosen recipe into the editor.
7. `can_discard()` compares the form with the saved recipe and asks
   before discarding changes when selecting, starting a recipe, or closing.
8. `delete_recipe()` confirms deletion and saves the shortened list.
   `main()` loads the data and starts Tkinter's event loop.

The `if __name__ == "__main__":` block starts the app when run directly,
while allowing imports without opening a window.

## Storage and Limitations

- The project folder must be writable. `recipes.json` is included as
  example data and is not ignored by Git. The app saves changes to this
  same file, so adding, editing, or deleting recipes changes its contents.
  If the file is missing, the app starts empty and creates it on save.
  The temporary save file, `recipes.tmp`, is ignored by Git.
- Back up `recipes.json` to keep a copy of your recipes. If it cannot be
  read or has invalid data, the app displays an error and closes without
  overwriting it. Back up and repair or rename the file before restarting.
- Use one running instance at a time; simultaneous instances can overwrite
  each other's changes.
- Titles can repeat. Recipes stay in insertion order and are selected by
  their position, so duplicate titles remain separate entries.
- Ingredients and instructions are plain text. The app does not calculate
  quantities, nutrition, or cooking times.
- Changes are saved only when you click **Save**. The discard prompt
  does not save them automatically.

## Ideas to Try Next

- Search recipes by title or ingredient
- Add categories such as breakfast, lunch, and dinner
- Export a recipe to a text file
- Scale ingredient quantities for different serving sizes

---

Project for learning purposes.
