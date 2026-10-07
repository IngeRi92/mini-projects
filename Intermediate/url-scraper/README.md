# URL Scraper

A simple command-line app that collects links from one webpage, displays
them, and saves them to a text file.

## Features

- Ask for a full website address starting with `http://` or `https://`
- Find links in HTML `<a href="...">` tags
- Convert relative links such as `/about` into full URLs
- Use the final page address after redirects and support HTML base URLs
- Remove duplicate URLs and sort the results
- Skip empty links, page-only anchors, and non-web links such as `mailto:`
- Remove fragments such as `#contact` while keeping query parameters
- Report download and file-saving errors

## How to Run

1. Make sure you have Python 3 installed.
2. From the project root, install the required packages:

   ```bash
   python -m pip install -r Intermediate/url-scraper/requirements.txt
   ```

3. Run the app:

   ```bash
   python Intermediate/url-scraper/url_scraper.py
   ```

   Or, from this folder, run `python url_scraper.py`.

4. Enter the full URL of the page you want to read.

Results are saved to `urls.txt` beside the script. Each successful run
with links replaces the previous file contents. If no links are found
or downloading fails, any previous output file is left unchanged.
Generated results are excluded from Git.

## Example

This illustrative page contains three links; actual results depend on
the HTML returned by the website.

```text
Welcome to URL Scraper!
Collect links from one webpage without visiting the linked pages.
Website URL: https://example.com

Found 3 unique links:
https://example.com/about
https://example.com/blog
https://example.com/contact

Saved links to C:\Projects\url-scraper\urls.txt
```

## How the Code Works

1. `is_web_url()` uses `urlparse()` to check the scheme and hostname.
   `get_url()` repeats the question until the input passes this check.
2. `fetch_page()` uses `requests.get()` to download the page. A timeout
   limits how long it waits for a connection or incoming data;
   `raise_for_status()` reports HTTP errors such as 404.
3. `extract_links()` uses Beautiful Soup to read the HTML and
   `find_all("a", href=True)` to find links. `urljoin()` turns relative
   addresses into full URLs. `urldefrag()` removes page fragments.
4. A `set` removes duplicate URL strings. `sorted()` turns the set into
   a list with a consistent order for display and saving.
5. `save_links()` writes each URL on its own line using UTF-8 encoding.
   The `with` statement closes the file automatically.
6. `main()` connects these steps and shows readable error messages.

The `if __name__ == "__main__":` block runs the app when started directly,
but lets other code import its functions without starting the prompts.

Library references: [Requests quickstart](https://requests.readthedocs.io/en/stable/user/quickstart/)
and [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Limitations

The app reads one page's returned HTML. It does not run JavaScript, log
in, or follow the links it finds. Links created only by JavaScript will
not appear. Both same-site and external links are included; collected
links are not checked to see whether they work.

## Ideas to Try Next

- Show only links belonging to the same website
- Let the user choose the output filename
- Save link text alongside each URL in a CSV file

---

Project for learning purposes.
