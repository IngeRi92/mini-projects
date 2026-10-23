"""Serve a personal portfolio website locally using Python's standard library."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


SITE_DIRECTORY = Path(__file__).resolve().parent / "site"
HOST = "127.0.0.1"


class PortfolioServer(ThreadingHTTPServer):
    """Keep a second server from sharing this port on Windows."""

    allow_reuse_address = False


def parse_port(text):
    """Convert a command-line value into a usable TCP port.

    Args:
        text (str): Port number supplied on the command line.

    Returns:
        int: A port between 1 and 65535.

    Raises:
        argparse.ArgumentTypeError: If the value is not a valid port.
    """
    try:
        port = int(text)
    except ValueError:
        raise argparse.ArgumentTypeError("Enter a whole-number port from 1 to 65535.") from None
    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError("Choose a port from 1 to 65535.")
    return port


def main():
    """Read the port option and serve the website until Ctrl+C is pressed.

    Returns:
        int: Zero on normal shutdown, or one if the server cannot start.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=parse_port, default=8000,
                        help="local port to use (default: 8000)")
    args = parser.parse_args()
    if not (SITE_DIRECTORY / "index.html").is_file():
        print(f"Cannot find {SITE_DIRECTORY / 'index.html'}. Restore the site folder.")
        return 1

    # Serve only the site folder, regardless of where the script is launched.
    handler = partial(SimpleHTTPRequestHandler, directory=str(SITE_DIRECTORY))
    try:
        with PortfolioServer((HOST, args.port), handler) as server:
            print(f"Portfolio: http://{HOST}:{args.port}", flush=True)
            print("Press Ctrl+C to stop.", flush=True)
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as error:
        print(f"Could not run the server: {error}")
        print("If the port is busy, try --port 8001.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
