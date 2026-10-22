# Expense Tracker

A small desktop app for recording your spending. You type in an expense, and the program shows it in a table with a running total and a total per category. Your data is saved in a JSON file, so it is still there next time.

## Features

- Add expenses with a date, category, description, and amount
- Table of all expenses with a scrollbar
- Total spent and totals per category, updated after every change
- Delete an expense (with a confirmation question)
- Data saved to `expenses.json` next to the script
- Input checks with clear error messages (bad date, bad amount, empty fields)
- Press Enter to add an expense
- Warns you before closing if you typed something that was not added yet

## How to Run

**Prerequisites**

- Python 3.9 or newer
- Tkinter (included with Python on Windows and macOS). On Debian/Ubuntu Linux, install it with:

```bash
sudo apt install python3-tk
```

No other packages are needed. The program uses only Python's standard library.

**From the repo root**

```bash
python <project-folder>/expense_tracker.py
```

**From the project folder**

```bash
cd <project-folder>
python expense_tracker.py
```

Replace `<project-folder>` with the real folder name of this project. On some systems the command is `python3` instead of `python`.

## Example of Use

1. Start the program. The date box already contains today's date.
2. Fill in the form:

   | Field       | Example     |
   |-------------|-------------|
   | Date        | 2026-10-22  |
   | Category    | food        |
   | Description | Groceries   |
   | Amount      | 23.40       |

3. Click **Add expense** or press Enter.

The table now shows the new row, and the bottom of the window shows:

```text
Total spent: 23.40
By category:
Food: 23.40
```

Note that "food" became "Food". Categories are capitalized so that "food" and "Food" are counted together.

The saved file `expenses.json` looks like this:

```json
[
  {
    "date": "2026-10-22",
    "category": "Food",
    "description": "Groceries",
    "amount_cents": 2340
  }
]
```

## How the Code Works

The file is organized from simple parts to the window that uses them.

**Pure functions** (they do not need a window, so they are easy to test)

- `parse_amount(text)` turns text such as `"12.50"` into `1250` cents. It uses a regular expression to accept only digits with an optional dot and one or two decimals.
- `format_amount(cents)` turns `1250` back into `"12.50"`.
- `validate_date(text)` and `validate_expense(expense)` check the data and raise `ValueError` with a message the user can understand.
- `totals_by_category(expenses)` adds up the cents for each category in a dictionary.

**File storage**

- `load_expenses(path)` reads the JSON file and validates every expense. A missing file simply means "no expenses yet".
- `save_expenses(path, expenses)` writes a temporary file first and then replaces the real file. If the program crashes while writing, your old data is not damaged.

**The window**

- `ExpenseTracker` builds the screen in small steps: `_build_form()`, `_build_table()`, `_build_footer()`. Each method does one job, and `refresh()` redraws the table and totals from `self.expenses`.
- `persist()` saves first and only then updates the screen. This way the screen never shows data that failed to save.
- `main()` loads the data and starts the window. If the file is broken, it shows an error and stops instead of opening an empty tracker, because the next save would overwrite the broken (but maybe fixable) file.

**Key concepts to notice**

- **Integer cents instead of decimals.** Floats cannot store 0.10 exactly (`0.1 + 0.2` gives `0.30000000000000004`). Whole numbers have no such problem.
- **Separating logic from the interface.** Checking and calculating live in plain functions, and the class only handles the window.
- **Safe saving.** Temporary file, then replace.

## Customization and Limitations

**Customization**

- Change the window size with `WINDOW_SIZE` and `MIN_WINDOW_SIZE` at the top of the file.
- Add or rename a form field in `FORM_FIELDS`, and a table column in `TABLE_COLUMNS`. A new field also needs a matching key in the saved data and in `validate_expense()`.
- Change where data is stored with `DATA_FILE`.

**Limitations**

- Amounts must use a dot (`12.50`), not a comma.
- All expenses are in one currency, and the currency is not shown.
- Expenses cannot be edited, only deleted and added again.
- The category summary is a label, so with very many categories it can grow taller than the window.
- Everything is kept in memory and saved as a whole file on each change. This is fine for hundreds of expenses, but not for huge amounts of data.

## Ideas to Try Next

- Write tests with `pytest` for `parse_amount`, `format_amount`, and `validate_expense`. Try inputs like `"12.999"`, `"0"`, and `"2026-02-30"`.
- Move the pure functions into their own file (for example `expenses_core.py`) and import them.
- Replace the Category box with a dropdown (`ttk.Combobox`) that remembers earlier categories.
- Add an **Edit** button for existing expenses.
- Filter the table by month or category.
- Show the category totals in a second table with a scrollbar.
- Export the expenses to a CSV file.

Project for learning purposes.