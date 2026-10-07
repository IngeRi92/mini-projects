"""Collect unique website links from one webpage and save them to a file."""

from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


def is_web_url(url):
    """Check whether a URL has an HTTP or HTTPS scheme and a hostname.

    Args:
        url (str): The address to check.

    Returns:
        bool: True for a basic web address. This does not check reachability.
    """
    try:
        parts = urlparse(url)
        return parts.scheme in ["http", "https"] and bool(parts.hostname)
    except ValueError:
        return False


def get_url():
    """Ask for a website address, retrying invalid input.

    Returns:
        str: An HTTP or HTTPS URL with a hostname.
    """
    while True:
        url = input("Website URL: ").strip()
        if is_web_url(url):
            return url
        print("Please enter a full URL, such as https://example.com.")


def fetch_page(url):
    """Download a page and check for HTTP errors.

    Args:
        url (str): The webpage address to request.

    Returns:
        tuple[bytes, str]: Page content and its final URL after redirects.

    Raises:
        requests.RequestException: If the request fails or times out.
    """
    # A timeout prevents waiting indefinitely when a server stops responding.
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.content, response.url


def extract_links(html, page_url):
    """Collect sorted, unique HTTP and HTTPS links from HTML.

    Args:
        html (str or bytes): The downloaded HTML content.
        page_url (str): The final page URL, used to complete relative links.

    Returns:
        list[str]: Full web URLs with fragment identifiers removed.
    """
    soup = BeautifulSoup(html, "html.parser")
    # A set keeps only one copy of each URL.
    links = set()

    # Some pages specify a different base address for relative links.
    base_tag = soup.find("base", href=True)
    if base_tag:
        try:
            base_url = urljoin(page_url, base_tag["href"].strip())
            if is_web_url(base_url):
                page_url = base_url
        except ValueError:
            pass

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        if not href or href.startswith("#"):
            continue
        try:
            # /about becomes a full URL; #section does not identify a new page.
            full_url = urljoin(page_url, href)
            full_url, fragment = urldefrag(full_url)
            if is_web_url(full_url):
                links.add(full_url)
        except ValueError:
            # Skip malformed links without losing the rest of the results.
            continue

    return sorted(links)


def save_links(links, output_path):
    """Write one URL per line, replacing previous contents of the file.

    Args:
        links (list[str]): The URLs to save.
        output_path (Path): The destination text file.

    Returns:
        None.

    Raises:
        OSError: If the output file cannot be written.
    """
    with output_path.open("w", encoding="utf-8") as file:
        for link in links:
            file.write(link + "\n")


def main():
    """Ask for one page, display its links, and save the results.

    Returns:
        None.
    """
    print("Welcome to URL Scraper!")
    print("Collect links from one webpage without visiting the linked pages.")
    url = get_url()
    try:
        html, page_url = fetch_page(url)
    except requests.RequestException as error:
        print(f"Could not load the page: {error}")
        return

    links = extract_links(html, page_url)
    if not links:
        print("No HTTP or HTTPS links found. No file was written.")
        return

    print(f"\nFound {len(links)} unique links:")
    for link in links:
        print(link)

    # Keep the output beside the script, regardless of the terminal folder.
    output_path = Path(__file__).resolve().parent / "urls.txt"
    try:
        save_links(links, output_path)
    except OSError as error:
        print(f"Could not save the links: {error}")
        return
    print(f"\nSaved links to {output_path}")


if __name__ == "__main__":
    main()
