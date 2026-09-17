"""Main application entry point.

Run this file with:
    python run.py
"""

import sys
import io

# Ensure UTF-8 output encoding across all operating systems and terminals (Windows cp1256 / Linux)
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

from app import create_app
from app.core.config import config

app = create_app()

if __name__ == "__main__":
    print("=" * 60)
    print(f"[*] Starting {config.APP_NAME} v{config.APP_VERSION}")
    print(f"[*] Server running at: http://{config.HOST}:{config.PORT}")
    print("=" * 60)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
