# File Organizer

A simple command-line app that sorts files into folders by file extension.
This first intermediate project uses only Python's standard library.

## Features

- Preview the proposed moves before making changes
- Move files only after entering `y` or `yes` (case-insensitive)
- Sort files into Images, Documents, Audio, Videos, Archives, and Other
- Recognize uppercase extensions such as `.JPG`
- Skip duplicate destination names, keeping the original file in place
- Leave subfolders, symbolic links, and the running script alone
- Report file errors and continue with the remaining files

## How to Run

1. Make sure you have Python 3 installed. No extra packages are needed.
2. From the project root, run:

   ```bash
   python Intermediate/file-organizer/file_organizer.py
   ```

   Or, from this folder, run `python file_organizer.py`.

3. Enter the path to the folder you want to organize. Paths with spaces
   are supported, including paths copied with surrounding double quotes.
   Relative paths start from the terminal's current folder.
4. Read the preview. Enter `y` or `yes` to move the files; any other
   response cancels without changing anything.

For your first run, create a practice folder containing copies of a few
files. The app moves files rather than copying them, and has no undo
command. Run one organizer at a time and avoid editing the chosen folder
while it runs.

## Example

```text
Welcome to File Organizer!
Sort files into category folders. Subfolders are left alone.
Folder to organize: C:\Users\Learner\Practice

Preview for C:\Users\Learner\Practice:
notes.txt -> Documents/notes.txt
photo.JPG -> Images/photo.JPG
song.mp3 -> Audio/song.mp3
Existing destination names will be skipped.

Move these files? (y/n): y

Moved: 3. Skipped: 0.
```

Category folders are created as needed inside the selected folder.
Unknown extensions and files without an extension go into `Other`.
Only the final extension is used: `backup.tar.gz` goes into `Archives`
because its final extension is `.gz`.

If `Documents/notes.txt` already exists, `notes.txt` stays where it is
and a skip message is shown. A category name occupied by a file causes
an error for that category; other categories can still be organized.
Category folders that are symbolic links are skipped.

## How the Code Works

1. `get_folder()` asks for a valid folder and returns a `Path` object.
2. `get_category()` looks up a file extension in the `CATEGORIES`
   dictionary. Add extensions there to customize the organizer.
3. `plan_moves()` builds a list of `(source, destination)` tuples.
   A tuple groups the two paths for each move. Planning changes nothing.
4. `main()` prints that plan and asks for confirmation.
5. `organize_files()` creates category folders and uses `shutil.move()`
   to move each file. It counts successful moves for the final summary.

`pathlib.Path` represents file and folder paths. The `/` operator joins
path parts, `suffix` reads an extension, and `iterdir()` lists direct
children. A `try`/`except OSError` block handles filesystem problems,
such as missing files or denied access, with a readable message.

The `if __name__ == "__main__":` block starts the app when the script is
run directly. It also lets other Python code import its functions without
starting the input prompts.

## Ideas to Try Next

- Add a new category and try files with matching extensions
- Rename duplicates automatically instead of skipping them
- Add a Tkinter interface with a folder picker

---

Project for learning purposes.
