# Basic Flask App

A simple Flask application built to learn core web development concepts: routing, HTTP methods, template rendering, and form handling.

## What this project demonstrates

- **Routing**: static, dynamic, and typed (`<int:id>`) URL routes
- **HTTP methods**: GET vs POST, and why they're used differently
- **Templates**: Jinja2 rendering (`render_template`, variables, loops, conditionals)
- **Form handling**: reading submitted data via `request.form`
- **PRG pattern** (Post-Redirect-Get): using `redirect()` and `url_for()` to avoid duplicate form submissions on refresh
- **CRUD operations**: full Create, Read, Update, Delete cycle on a `/tasks` resource

## Routes

| Route                         | Method    | Description                           |
| ----------------------------- | --------- | ------------------------------------- |
| `/`                           | GET       | Welcome message                       |
| `/hello/<name>`               | GET       | Greets a user by name (URL parameter) |
| `/hello`                      | GET, POST | Form-based greeting                   |
| `/tasks`                      | GET       | Lists all tasks                       |
| `/tasks`                      | POST      | Adds a new task                       |
| `/tasks/<int:task_id>/done`   | POST      | Toggles a task's completed status     |
| `/tasks/<int:task_id>/delete` | POST      | Deletes a task                        |

## Design note

A "pure" REST API would use `PUT`/`PATCH` and `DELETE` HTTP methods directly on `/tasks/<id>`. Since HTML `<form>` elements only support `GET` and `POST`, this project uses the common pragmatic pattern of encoding the action in the URL (`/tasks/<id>/delete`) instead. A JavaScript-based version (using `fetch`) could implement the stricter REST convention.

## Notes

- Data is stored in-memory (a Python list) and resets when the server restarts. Persistent storage (e.g. SQLite) is planned for an intermediate-level project.
- Built as part of a structured 60-project Python roadmap.

## How to run

```
pip install flask
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.
