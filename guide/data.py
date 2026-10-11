"""Navigation metadata only; chapter prose remains hardcoded in templates."""

CHAPTERS = [
    {"number": "01", "url_name": "guide:chapter-01", "slug": "world-rules-responsibilities", "title": "World, Rules and Responsibilities", "phase": "DOMAIN"},
    {"number": "02", "url_name": "guide:chapter-02", "slug": "tkinter-turtle-interface", "title": "Tkinter and Turtle: The Garden Interface", "phase": "PRESENTATION"},
    {"number": "03", "url_name": "guide:chapter-03", "slug": "async-events-concurrency", "title": "Async, Events and Concurrency", "phase": "RUNTIME"},
    {"number": "04", "url_name": "guide:chapter-04", "slug": "ollama-litellm", "title": "Local AI with Ollama and LiteLLM", "phase": "INTELLIGENCE"},
    {"number": "05", "url_name": "guide:chapter-05", "slug": "agent-tools-safe-execution", "title": "The First Agent, Tools and Safe Execution", "phase": "AGENCY"},
    {"number": "06", "url_name": "guide:chapter-06", "slug": "memory-sqlite", "title": "Memory, Recall and SQLite Persistence", "phase": "MEMORY"},
    {"number": "07", "url_name": "guide:chapter-07", "slug": "agent-communication", "title": "Communication Between Agents", "phase": "MULTI-AGENT"},
    {"number": "08", "url_name": "guide:chapter-08", "slug": "contracts-reliability", "title": "Contracts, Standards and Reliability", "phase": "QUALITY"},
    {"number": "09", "url_name": "guide:chapter-09", "slug": "experiments-simulation", "title": "Artificial-Life Experiments", "phase": "RESEARCH"},
]


def chapter_context(number: str) -> dict:
    """Return current, previous and next metadata for a chapter page."""
    index = next(i for i, item in enumerate(CHAPTERS) if item["number"] == number)
    return {
        "chapter": CHAPTERS[index],
        "previous_chapter": CHAPTERS[index - 1] if index else None,
        "next_chapter": CHAPTERS[index + 1] if index < len(CHAPTERS) - 1 else None,
    }
