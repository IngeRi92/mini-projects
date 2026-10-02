"""A command-line app for sorting files into folders by their extension."""

from pathlib import Path
import shutil


# A dictionary connects each folder name to its supported file extensions.
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".txt", ".doc", ".docx", ".csv", ".xlsx"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".gz", ".7z"],
}


def get_folder():
    """Ask for an existing folder, retrying when the path is invalid.

    Returns:
        Path: The selected folder as an absolute path.
    """
    while True:
        folder_input = input("Folder to organize: ").strip().strip('"')
        if not folder_input:
            print("Please enter a folder path.")
            continue
        try:
            folder = Path(folder_input).expanduser().resolve()
            if folder.is_dir():
                return folder
        except (OSError, RuntimeError, ValueError):
            pass
        print("That folder could not be found. Please try again.")


def get_category(file_path):
    """Find a file's category using its final extension.

    Args:
        file_path (Path): The file to classify.

    Returns:
        str: A category folder name, or 'Other' for unknown extensions.
    """
    # Lowercase makes .JPG and .jpg belong to the same category.
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"


def plan_moves(folder):
    """Collect proposed moves without creating folders or moving files.

    Only direct child files are included. Skip folders, symbolic links,
    and this script so the running program does not move itself.

    Args:
        folder (Path): The folder to organize.

    Returns:
        list[tuple[Path, Path]]: Pairs of source and destination paths.

    Raises:
        OSError: If the folder contents cannot be read.
    """
    moves = []
    script_path = Path(__file__).resolve()
    for source in sorted(folder.iterdir()):
        if source.is_symlink() or not source.is_file():
            continue
        if source.resolve() == script_path:
            continue
        destination = folder / get_category(source) / source.name
        moves.append((source, destination))
    return moves


def organize_files(moves):
    """Perform the planned moves and report skipped files.

    Existing destination names are skipped. Errors for one file do not
    stop the remaining moves. Run one organizer at a time and avoid
    changing the selected folder while it is being organized.

    Args:
        moves (list[tuple[Path, Path]]): Source and destination pairs.

    Returns:
        int: The number of files successfully moved.
    """
    moved_count = 0
    for source, destination in moves:
        try:
            if source.is_symlink() or not source.is_file():
                print(f"Skipped {source.name}: source is no longer a regular file.")
                continue
            # Do not follow category links to a different folder.
            if destination.parent.is_symlink():
                print(f"Skipped {source.name}: category folder is a symbolic link.")
                continue
            if destination.exists() or destination.is_symlink():
                print(f"Skipped {source.name}: destination name already exists.")
                continue
            destination.parent.mkdir(exist_ok=True)
            shutil.move(str(source), str(destination))
            moved_count += 1
        except OSError as error:
            print(f"Could not move {source.name}: {error}")
    return moved_count


def main():
    """Preview the selected folder and organize it only after confirmation.

    Returns:
        None.
    """
    print("Welcome to File Organizer!")
    print("Sort files into category folders. Subfolders are left alone.")
    folder = get_folder()
    try:
        moves = plan_moves(folder)
    except OSError as error:
        print(f"Could not read the folder: {error}")
        return

    if not moves:
        print("No files to organize.")
        return

    print(f"\nPreview for {folder}:")
    for source, destination in moves:
        print(f"{source.name} -> {destination.parent.name}/{destination.name}")
    print("Existing destination names will be skipped.")

    answer = input("\nMove these files? (y/n): ").strip().lower()
    if answer not in ["y", "yes"]:
        print("Cancelled. No files were moved.")
        return

    moved_count = organize_files(moves)
    print(f"\nMoved: {moved_count}. Skipped: {len(moves) - moved_count}.")


if __name__ == "__main__":
    main()
