"""A command-line app for downloading images from direct HTTP or HTTPS URLs."""

from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


DOWNLOAD_FOLDER = Path(__file__).resolve().parent / "downloads"
MAX_IMAGE_SIZE = 20 * 1024 * 1024
IMAGE_EXTENSIONS = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/bmp": ".bmp",
    "image/tiff": ".tiff",
    "image/avif": ".avif",
    "image/x-icon": ".ico",
    "image/vnd.microsoft.icon": ".ico",
}


def get_image_url():
    """Ask for a direct image URL, retrying until its format is valid.

    Returns:
        str: An HTTP or HTTPS URL with a hostname, or an empty string
            when the user presses Enter to quit.
    """
    while True:
        url = input("Image URL (Enter to quit): ").strip()
        if not url:
            return ""
        try:
            parts = urlsplit(url)
            if parts.scheme in ("http", "https") and parts.hostname:
                return url
        except ValueError:
            pass
        print("Please enter a full URL starting with http:// or https://.")


def save_image(data, extension, folder):
    """Save downloaded bytes using the first available numbered filename.

    Args:
        data (bytes): The downloaded image contents.
        extension (str): A file extension from IMAGE_EXTENSIONS.
        folder (Path): Destination directory, created if it does not exist.

    Returns:
        Path: The saved image's path, such as downloads/image_1.png.

    Raises:
        OSError: If the directory or file cannot be written.
    """
    folder.mkdir(parents=True, exist_ok=True)
    number = 1
    while True:
        path = folder / f"image_{number}{extension}"
        try:
            # Exclusive creation protects files from previous downloads.
            image_file = path.open("xb")
        except FileExistsError:
            number += 1
            continue
        try:
            with image_file:
                image_file.write(data)
        except BaseException:
            # Remove our incomplete file if writing fails or is interrupted.
            path.unlink(missing_ok=True)
            raise
        return path


def download_image(url, folder=DOWNLOAD_FOLDER):
    """Download one image, checking its reported type and limiting its size.

    Args:
        url (str): A direct HTTP or HTTPS image URL.
        folder (Path): Destination directory. Defaults to the downloads
            folder beside this script.

    Returns:
        Path: The saved image's path.

    Raises:
        ValueError: If the URL is invalid, the reported image type is
            unsupported, or the response is empty or larger than 20 MiB.
        URLError: If the server cannot be reached or returns an HTTP error.
        OSError: If a network or file operation fails.
    """
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        raise ValueError("Use a full HTTP or HTTPS image URL.")

    request = Request(url, headers={"User-Agent": "Python-Image-Downloader/1.0"})
    with urlopen(request, timeout=30) as response:
        content_type = response.headers.get_content_type()
        extension = IMAGE_EXTENSIONS.get(content_type)
        if extension is None:
            raise ValueError(
                "The server did not report a supported image type. "
                "Use a direct image link, not a webpage."
            )
        # Reading one extra byte lets us detect oversized responses while
        # keeping memory use bounded even without a Content-Length header.
        data = response.read(MAX_IMAGE_SIZE + 1)
        if not data:
            raise ValueError("The server returned an empty image.")
        if len(data) > MAX_IMAGE_SIZE:
            raise ValueError("The image exceeds the 20 MiB download limit.")

    return save_image(data, extension, folder)


def main():
    """Download images interactively until the user chooses to quit.

    Show a helpful message after a failed download and allow another URL.
    Entering 'y' or 'yes' after a successful download starts another one.

    Returns:
        None.
    """
    print("Welcome to Image Downloader!")
    print("Paste a direct image URL to save it to the downloads folder.")
    try:
        while True:
            url = get_image_url()
            if not url:
                break
            try:
                path = download_image(url)
            except (ValueError, URLError, OSError) as error:
                print(f"Download failed: {error}")
                continue
            print(f"Saved: {path}")
            if input("\nDownload another? (y/n): ").strip().lower() not in ("y", "yes"):
                break
            print()
    except (KeyboardInterrupt, EOFError):
        print()
    print("Thanks for using Image Downloader!")


if __name__ == "__main__":
    main()
