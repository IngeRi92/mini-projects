"""Track expenses in a Tkinter window with local JSON storage."""

from datetime import date
import json
from pathlib import Path
import re
import tkinter as tk
from tkinter import messagebox, ttk

# --- Settings -------------------------------------------------------------
# Keeping these at the top means you can change the look or the data location
# without searching through the code.

# Path(__file__) is this script, so the data file always sits next to it,
# no matter which folder you start the program from.
DATA_FILE = Path(__file__).resolve().with_name("expenses.json")

WINDOW_SIZE = "800x600"
MIN_WINDOW_SIZE = (650, 500)

# (key, label shown next to the input box)
FORM_FIELDS = (
    ("date", "Date (YYYY-MM-DD)"),
    ("category", "Category"),
    ("description", "Description"),
    ("amount", "Amount (for example, 12.50)"),
)

# (key, column title, width in pixels)
TABLE_COLUMNS = (
    ("date", "Date", 110),
    ("category", "Category", 140),
    ("description", "Description", 280),
    ("amount", "Amount", 100),
)

# Fields in a saved expense that must be non-empty text.
REQUIRED_TEXT_FIELDS = ("date", "category", "description")


# --- Pure functions -------------------------------------------------------
# These do not use the window, so they are easy to test on their own.

def parse_amount(text):
    """Convert a positive decimal amount to integer cents.

    Args:
        text (str): Amount using a dot and at most two decimal places.

    Returns:
        int: The amount in cents, for example 1250 for "12.50".

    Raises:
        ValueError: If the amount is invalid or not positive.
    """
    text = text.strip()
    # Only digits, optionally followed by a dot and 1-2 digits.
    # This also rejects negative numbers, commas, and letters.
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", text):
        raise ValueError("Enter an amount such as 12 or 12.50 (up to two decimals).")
    whole, _, fraction = text.partition(".")
    # ljust pads "5" to "50", so "12.5" means 12.50 and not 12.05.
    cents = int(whole) * 100 + int(fraction.ljust(2, "0"))
    if cents <= 0:
        raise ValueError("The amount must be greater than zero.")
    return cents


def format_amount(cents):
    """Display integer cents as text without floating-point rounding.

    Args:
        cents (int): A nonnegative amount in cents.

    Returns:
        str: The amount with two decimal places, for example "12.05".
    """
    # // is integer division and % gives the remainder: 1205 -> 12 and 5.
    return f"{cents // 100}.{cents % 100:02d}"


def validate_date(text):
    """Check that text is a real calendar date written as YYYY-MM-DD.

    Args:
        text (str): The date text to check.

    Raises:
        ValueError: If the format is wrong or the date does not exist.
    """
    # The regex looks redundant, but it is not: since Python 3.11,
    # date.fromisoformat() also accepts forms like "20261022".
    # The regex enforces our one strict format, so do not remove it.
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", text):
        raise ValueError("Enter the date as YYYY-MM-DD.")
    try:
        date.fromisoformat(text)  # Rejects impossible dates like 2026-02-30.
    except ValueError:
        raise ValueError("Enter a valid calendar date as YYYY-MM-DD.")


def validate_expense(expense):
    """Check the required fields of one expense.

    Args:
        expense (dict): Date, category, description, and amount_cents fields.

    Raises:
        ValueError: If a field is missing or invalid.
    """
    if not isinstance(expense, dict):
        raise ValueError("Each expense must be an object.")

    for key in REQUIRED_TEXT_FIELDS:
        value = expense.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Each expense needs a {key}.")

    validate_date(expense["date"])

    amount = expense.get("amount_cents")
    # bool is a subclass of int, so isinstance(True, int) is True.
    # Checking type() exactly keeps True and False out of the amount.
    if type(amount) is not int or amount <= 0:
        raise ValueError("Each expense needs a positive whole number of cents.")


def totals_by_category(expenses):
    """Add up the cents spent in each category.

    Args:
        expenses (list): Validated expense dictionaries.

    Returns:
        dict: Maps each category name to its total in cents.
    """
    totals = {}
    for expense in expenses:
        category = expense["category"]
        # .get(category, 0) starts a new category at zero.
        totals[category] = totals.get(category, 0) + expense["amount_cents"]
    return totals


# --- File storage ---------------------------------------------------------

def load_expenses(path):
    """Read and validate saved expenses, starting empty if the file is missing.

    Args:
        path (Path): The JSON file to read.

    Returns:
        list: Validated expense dictionaries.

    Raises:
        OSError: If reading fails.
        ValueError: If JSON, UTF-8, or expense data is invalid.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []  # First run: nothing saved yet, which is not an error.
    # json.JSONDecodeError is a kind of ValueError, so bad JSON is covered.
    expenses = json.loads(text)
    if not isinstance(expenses, list):
        raise ValueError("Expense data must be a list.")
    for expense in expenses:
        validate_expense(expense)
    return expenses


def save_expenses(path, expenses):
    """Write a temporary file, then replace the saved file with it.

    If the program crashes while writing, the real file is still intact.
    Writing straight into the real file could leave it half-written.

    Args:
        path (Path): The destination JSON file.
        expenses (list): Validated expense dictionaries.

    Raises:
        OSError: If writing or replacing the file fails.
    """
    temporary_path = path.with_suffix(".tmp")
    temporary_path.write_text(
        # ensure_ascii=False keeps characters like "õ" readable in the file.
        json.dumps(expenses, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary_path.replace(path)


# --- The window -----------------------------------------------------------

class ExpenseTracker:
    """The main window: input form, expense table, and totals."""

    def __init__(self, root, expenses, path=DATA_FILE):
        """Set up the window and fill it with the loaded expenses.

        Args:
            root (tk.Tk): The application window.
            expenses (list): Validated expense dictionaries.
            path (Path): The file used for saving.
        """
        self.root = root
        self.expenses = expenses
        self.path = path

        root.title("Expense Tracker")
        root.geometry(WINDOW_SIZE)
        root.minsize(*MIN_WINDOW_SIZE)
        # Run our own close() when the user clicks the window's X button.
        root.protocol("WM_DELETE_WINDOW", self.close)
        # Pressing Enter anywhere in the window adds the expense.
        root.bind("<Return>", lambda event: self.add_expense())

        self._build_form()
        self._build_table()
        self._build_footer()
        self.refresh()

    # Methods starting with _ are helpers used only inside this class.

    def _build_form(self):
        """Create the input boxes and the Add button."""
        form = ttk.Frame(self.root, padding=10)
        form.pack(fill="x")
        form.columnconfigure(1, weight=1)  # Let the input column stretch.

        # Keep each Entry in a dict so other methods can read it by key.
        self.fields = {}
        for row, (key, label) in enumerate(FORM_FIELDS):
            ttk.Label(form, text=label).grid(row=row, column=0, sticky="w", padx=(0, 10))
            entry = ttk.Entry(form)
            entry.grid(row=row, column=1, sticky="ew", pady=3)
            self.fields[key] = entry

        self.fields["date"].insert(0, date.today().isoformat())
        ttk.Button(form, text="Add expense", command=self.add_expense).grid(
            row=len(FORM_FIELDS), column=1, sticky="w", pady=5,
        )

    def _build_table(self):
        """Create the expense table with a scrollbar."""
        frame = ttk.Frame(self.root, padding=(10, 0))
        frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(
            frame,
            columns=[key for key, _, _ in TABLE_COLUMNS],
            show="headings",  # Hide the extra tree column we do not use.
            selectmode="browse",  # Only one row can be selected at a time.
            height=8,
        )
        for key, title, width in TABLE_COLUMNS:
            self.table.heading(key, text=title)
            self.table.column(
                key, width=width, minwidth=70,
                anchor="e" if key == "amount" else "w",  # Numbers line up on the right.
            )
        self.table.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.table.yview)
        scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=scrollbar.set)

    def _build_footer(self):
        """Create the Delete button and the totals labels."""
        ttk.Button(self.root, text="Delete selected", command=self.delete_expense).pack(pady=5)
        self.total_label = ttk.Label(self.root, padding=(10, 5))
        self.total_label.pack(anchor="w")
        self.summary_label = ttk.Label(self.root, padding=(10, 0, 10, 10), justify="left")
        self.summary_label.pack(anchor="w")

    def refresh(self):
        """Redraw the table and totals from self.expenses."""
        for item in self.table.get_children():
            self.table.delete(item)
        for index, expense in enumerate(self.expenses):
            # The row id is the list position, so we can find the expense later.
            self.table.insert("", "end", iid=str(index), values=(
                expense["date"],
                expense["category"],
                expense["description"],
                format_amount(expense["amount_cents"]),
            ))

        totals = totals_by_category(self.expenses)
        self.total_label.config(text=f"Total spent: {format_amount(sum(totals.values()))}")
        lines = [f"{category}: {format_amount(cents)}"
                 for category, cents in sorted(totals.items())]
        self.summary_label.config(text="By category:\n" + ("\n".join(lines) or "No expenses yet."))

    def persist(self, expenses):
        """Save a proposed collection, then update the screen.

        Saving first means the screen never shows data that failed to save.

        Args:
            expenses (list): The proposed expense collection.

        Returns:
            bool: Whether saving succeeded.
        """
        try:
            save_expenses(self.path, expenses)
        except OSError as error:
            messagebox.showerror(
                "Could not save", f"Your changes were not saved.\n\n{error}", parent=self.root,
            )
            return False
        self.expenses = expenses
        self.refresh()
        return True

    def add_expense(self):
        """Validate the form and save a new expense, clearing it only on success."""
        expense = {key: self.fields[key].get().strip() for key in REQUIRED_TEXT_FIELDS}
        # "food", "Food" and "FOOD" should count as one category.
        expense["category"] = expense["category"].title()
        try:
            expense["amount_cents"] = parse_amount(self.fields["amount"].get())
            validate_expense(expense)
        except ValueError as error:
            messagebox.showwarning("Invalid expense", str(error), parent=self.root)
            return

        # Build a new list instead of changing the old one, so a failed save
        # leaves self.expenses untouched.
        if self.persist(self.expenses + [expense]):
            self._clear_form()

    def _clear_form(self):
        """Empty the boxes after a successful save, keeping the date."""
        for key in ("category", "description", "amount"):
            self.fields[key].delete(0, "end")
        self.fields["description"].focus_set()

    def delete_expense(self):
        """Ask for confirmation, then delete the selected expense."""
        selection = self.table.selection()
        if not selection:
            messagebox.showinfo("No selection", "Select an expense to delete.", parent=self.root)
            return

        index = int(selection[0])
        description = self.expenses[index]["description"]
        if not messagebox.askyesno("Delete expense", f'Delete "{description}"?', parent=self.root):
            return

        updated = self.expenses.copy()
        del updated[index]
        self.persist(updated)

    def has_unsaved_input(self):
        """Check whether the user typed something that was not added yet.

        Returns:
            bool: True if category, description, or amount is not empty.
        """
        return any(self.fields[key].get().strip()
                   for key in ("category", "description", "amount"))

    def close(self):
        """Close the window, asking first if typed input would be lost."""
        if self.has_unsaved_input() and not messagebox.askyesno(
            "Unsaved expense", "Discard the expense in the form?", parent=self.root,
        ):
            return
        self.root.destroy()


def main():
    """Load saved expenses and start the GUI, or explain a loading error."""
    root = tk.Tk()
    root.withdraw()  # Hide the empty window while loading (an error may appear).
    try:
        expenses = load_expenses(DATA_FILE)
    except (OSError, ValueError) as error:
        messagebox.showerror(
            "Could not load expenses",
            f"{DATA_FILE}\n\n{error}\n\nBack up and repair or rename this file, then restart.",
            parent=root,
        )
        # Do not open an empty tracker: the next save would overwrite the
        # user's unreadable (but possibly recoverable) data.
        root.destroy()
        return
    ExpenseTracker(root, expenses)
    root.deiconify()  # Show the window now that loading worked.
    root.mainloop()


if __name__ == "__main__":
    main()