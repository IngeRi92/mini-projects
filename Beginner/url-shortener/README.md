# URL Shortener

A beginner Flask app that turns a URL into a numbered local link.

## How to Run

1. Install Python 3.9 or newer.
2. From the project root, run:

   ```bash
   python -m pip install -r Beginner/url-shortener/requirements.txt
   python Beginner/url-shortener/url_shortener.py
   ```

3. Open <http://127.0.0.1:5000> in your browser.
4. Enter a URL starting with `http://` or `https://` and click **Shorten**.
5. Click the generated link to open the original URL.

For example, the first link is `http://127.0.0.1:5000/s/1`.
Press `Ctrl+C` in the terminal to stop the app.

Links work only on your computer while the app is running. They are stored
in a Python dictionary and disappear when the app stops. Each submission
gets a new number. The app only checks the URL prefix, not whether the
website exists. A local link may be longer than an already short URL.

## How It Works

- `links` is a dictionary that matches a number to an original URL.
- `home()` displays the form and adds submitted URLs to the dictionary.
- `follow_link()` looks up a number and redirects to its original URL.
- `PAGE` contains the small HTML form shown in the browser.

This project practices dictionaries, functions, and basic Flask routes.

---

Project for learning purposes.
