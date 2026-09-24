"""A beginner URL shortener that stores links until the app stops."""

from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
links = {}  # Match each short code to its original URL.

PAGE = """
<h1>URL Shortener</h1>
<form method="post">
    <label for="url">Enter an HTTP or HTTPS URL:</label>
    <input id="url" name="url" type="url" required>
    <button type="submit">Shorten</button>
</form>
{% if short_url %}
<p>Your short link: <a href="{{ short_url }}">{{ short_url }}</a></p>
{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def home():
    """Show the form and store a URL when the user submits it.

    Returns:
        str: The page containing the form and any new short link.
    """
    short_url = None
    if request.method == "POST":
        destination = request.form.get("url", "").strip()
        if not destination.startswith(("http://", "https://")):
            return "Please enter a URL starting with http:// or https://."
        # Number links in order: 1, 2, 3, and so on.
        code = str(len(links) + 1)
        links[code] = destination
        short_url = url_for("follow_link", code=code, _external=True)
    return render_template_string(PAGE, short_url=short_url)


@app.route("/s/<code>")
def follow_link(code):
    """Open the original URL for a short code.

    Args:
        code (str): The number at the end of the short link.

    Returns:
        Response or tuple: A redirect, or an error message with status 404.
    """
    if code not in links:
        return "Short link not found.", 404
    return redirect(links[code])


if __name__ == "__main__":
    app.run()
