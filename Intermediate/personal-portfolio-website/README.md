# Personal Portfolio Website

A simple portfolio website served by a small Python program. Introduce
yourself, share your skills, and showcase projects with responsive HTML
and CSS. The sample content uses projects from this repository.

## Features

- About, skills, selected projects, and contact sections
- Project links to the learning portfolio on GitHub
- Layout that stacks into one column on smaller screens
- Keyboard focus styles, a skip link, and reduced-motion support
- Local Python server with a configurable port and startup error messages
- No third-party packages, JavaScript, or build step

## How to Run

**Prerequisites**

Python 3.9 or newer and a web browser. Only Python's standard library is
needed.

**From the repo root** (the folder containing `Beginner` and `Intermediate`)

```bash
python Intermediate/personal-portfolio-website/personal_portfolio.py
```

**From the project folder**

```bash
cd Intermediate/personal-portfolio-website
python personal_portfolio.py
```

Open **http://127.0.0.1:8000** in your browser. Press **Ctrl+C** in the
terminal to stop the server. On some systems use `python3` instead of
`python`.

If port 8000 is already in use, choose another port:

```bash
python personal_portfolio.py --port 8001
```

Then open **http://127.0.0.1:8001**. Use `--help` to see the available option.

## Example of Use

1. Run the Python script. The terminal shows:

   ```text
   Portfolio: http://127.0.0.1:8000
   Press Ctrl+C to stop.
   ```

2. Open that address to see the introduction and selected projects.
3. Click **Explore my projects** to jump to the project section.
4. Follow a project link to read its code on GitHub.
5. Edit `site/index.html`, save it, and refresh the browser to see changes.

The terminal also logs browser requests. A missing file returns HTTP 404;
a browser may request a favicon that this project does not include.

## How the Code Works

- `parse_port(text)` converts the command-line argument to an integer
  between 1 and 65535. `argparse` displays an error for invalid input.
- `main()` checks that the homepage exists, starts a
  `PortfolioServer`, and handles startup errors and Ctrl+C. This small
  `ThreadingHTTPServer` subclass disables address reuse so that Windows
  reports an occupied port instead of letting two servers share it.
- `SimpleHTTPRequestHandler` serves files and supplies their content
  types. `partial()` supplies the site directory whenever the server
  creates a handler for a request.
- `Path(__file__)` locates the site folder beside the script, so launching
  from another directory still works. Only that folder is served.
- The `with` statement closes the server socket when the program exits.
- `site/index.html` defines the content using semantic elements such as
  `nav`, `main`, `section`, and `article`. Links beginning with `#` jump to
  elements with matching IDs.
- `site/styles.css` controls colors, spacing, and layout. CSS Grid places
  the projects in columns; a media query stacks them on narrow screens.

Python handles HTTP requests; the browser renders HTML and CSS. Keeping
these responsibilities in separate files makes each easier to learn.

## Customization and Limitations

- Replace my name, the sample introduction, and email in the HTML. 
  Update both the email link's `href="mailto:..."` and its visible text.
- Update the project descriptions and GitHub links for your own projects.
  To add another project, copy an `article` inside the `projects` div.
- Change the colors using the variables at the top of `styles.css`.
- The email link opens a configured email app. It does not send mail
  itself, and the supplied address is only a placeholder.
- The page works offline; GitHub links require internet access. Project
  URLs follow this repository's existing GitHub address and assume the
  project folders have been pushed to its `main` branch.
- The server binds to `127.0.0.1`, so only your computer can access it.
  Python's basic HTTP server is for local learning, not production hosting.
- No form submissions, database, or automatic project discovery are
  included. Content is edited directly in the HTML file.

## Ideas to Try Next

- Add a profile photo with descriptive alternative text
- Add a downloadable resume
- Generate project entries from Python dictionaries
- Rebuild the page with Flask templates to learn server-side rendering
- Publish the static `site` folder with a static hosting service

Project for learning purposes.
