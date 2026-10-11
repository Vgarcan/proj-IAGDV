"""Export the hardcoded Django guide as a static Sites-compatible preview."""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

# Direct script execution places /scripts on sys.path; add the project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_core.settings")

import django  # noqa: E402
from django.conf import settings  # noqa: E402
from django.test import Client  # noqa: E402
from django.urls import reverse  # noqa: E402

from guide.data import CHAPTERS  # noqa: E402


def export_page(client: Client, route: str, destination: Path) -> None:
    """Render one Django route and write its complete HTML response."""
    response = client.get(route, HTTP_HOST="localhost")
    if response.status_code != 200:
        raise RuntimeError(f"Could not export {route}: HTTP {response.status_code}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(response.content)


def main() -> None:
    """Export the landing page, chapter pages and static assets."""
    django.setup()
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "_site_export").resolve()
    target.mkdir(parents=True, exist_ok=True)
    client = Client()

    export_page(client, reverse("main:home"), target / "index.html")
    for chapter in CHAPTERS:
        route = reverse(chapter["url_name"])
        export_page(client, route, target / route.lstrip("/") / "index.html")

    static_target = target / "static"
    if static_target.exists():
        shutil.rmtree(static_target)
    shutil.copytree(settings.BASE_DIR / "static", static_target)
    print(f"Exported {1 + len(CHAPTERS)} pages to {target}")


if __name__ == "__main__":
    main()
