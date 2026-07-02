# Basic Flask App

A simple Flask application built to learn core web development concepts: routing, HTTP methods, template rendering, and form handling.

## What this project demonstrates

- **Routing**: static (`/`) and dynamic (`/hello/<name>`) URL routes
- **HTTP methods**: GET vs POST, and why they're used differently
- **Templates**: Jinja2 rendering (`render_template`, variables, loops, conditionals)
- **Form handling**: reading submitted data via `request.form`
- **PRG pattern** (Post-Redirect-Get): using `redirect()` and `url_for()` to avoid duplicate form submissions on refresh
- **Early REST/CRUD concepts**: `/tasks` endpoint implements Create (`POST`) and Read (`GET`) — Update and Delete are planned next steps toward a full CRUD implementation

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Welcome message |
| `/hello/<name>` | GET | Greets a user by name (URL parameter) |
| `/hello` | GET, POST | Form-based greeting |
| `/tasks` | GET | Lists all tasks |
| `/tasks` | POST | Adds a new task |

## Notes

- Data is stored in-memory (a Python list) and resets when the server restarts. Persistent storage (e.g. SQLite) is planned for an intermediate-level project.
- Built as part of a structured 60-project Python roadmap.

## How to run

```bash
pip install flask
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Next steps

- Add `PUT`/`PATCH` and `DELETE` routes to complete the CRUD model
- Add basic form validation