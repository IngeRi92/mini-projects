# Image Downloader

A simple command-line app for downloading images from direct URLs in Python.

## Features

- Download an image from an HTTP or HTTPS URL
- Supports JPEG, PNG, GIF, WebP, BMP, TIFF, AVIF, and ICO responses
- Saves images in a `downloads` folder beside the script
- Uses numbered filenames such as `image_1.png` to avoid overwriting files
- Handles invalid links, network errors, and file permission errors
- Rejects empty responses and downloads larger than 20 MiB
- Download another image without restarting the program

## How to Run

1. Make sure you have Python 3.8 or newer installed. No extra packages are needed.
2. From the project root, run:

   ```bash
   python Beginner/image-downloader/image_downloader.py
   ```

   Or, from this folder, run `python image_downloader.py`.

3. Paste a direct image URL. You can usually get this by right-clicking an
   image in your browser and selecting **Copy image address**.

## Example

```text
Welcome to Image Downloader!
Paste a direct image URL to save it to the downloads folder.
Image URL (Enter to quit): https://example.com/photo.png
Saved: .../image-downloader/downloads/image_1.png

Download another? (y/n): n
Thanks for using Image Downloader!
```

The URL above is illustrative; replace it with a working direct image link.
The program prints the full path of the saved file. Enter `y` or `yes` to
download another image, or press Enter at the URL prompt to quit.

The file extension comes from the server's `Content-Type` header. The app
checks that header, but does not decode the image to verify its contents.
Webpage links and unsupported or missing image types are rejected. Some
websites block downloads or require sign-in. Network operations use a
30-second timeout; this is not a time limit for the entire download.

## What You Can Learn

- Using `urllib.request` to make HTTP requests and read response headers
- Working with folders and binary files using `pathlib`
- Handling exceptions and validating user input
- Organizing code into functions with `Args`, `Returns`, and `Raises` docstrings

---

Project for learning purposes.
