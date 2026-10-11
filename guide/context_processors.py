"""Template context shared by the guide navigation."""

from .data import CHAPTERS


def guide_navigation(request):
    """Expose ordered chapter metadata to base templates and partials."""
    return {"guide_chapters": CHAPTERS}
