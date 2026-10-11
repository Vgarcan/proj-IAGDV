# Project In-A-Gadda-Da-Vida

A Django learning guide for building an artificial-life laboratory with Python, Tkinter, Turtle, asyncio, Ollama, LiteLLM, safe tools, SQLite memory and multi-agent communication.

The visible project name uses the established spelling **In-A-Gadda-Da-Vida**, a playful reference to “In the Garden of Eden”. The technical Python package uses the safe identifier `gadda_da_vida` only when one is needed; the Django configuration package remains `_core`.

> Independent educational project. It is not affiliated with Iron Butterfly or any record label.

## Table of contents

1. [Purpose](#purpose)
2. [Architecture](#architecture)
3. [Template strategy](#template-strategy)
4. [Chapters](#chapters)
5. [Local setup](#local-setup)
6. [Tests](#tests)
7. [Project structure](#project-structure)
8. [Interface and accessibility](#interface-and-accessibility)
9. [Production notes](#production-notes)

## Purpose

The site turns the original Spanish learning material into an English, presentation-led guide. The prose for every chapter is hardcoded in a dedicated Django template. There is no CMS, database-backed article model or generic blog engine.

## Architecture

- `_core/` contains settings, root URLs and server entry points.
- `main/` owns the landing page.
- `guide/` owns explicit chapter routes, navigation metadata and chapter templates.
- `templates/partials/` contains shared navigation, footer, sidebar, header and previous/next controls.
- `static/` contains the Eden laboratory theme, restrained parallax behaviour and image assets.

## Template strategy

`templates/base.html` provides the document shell. `guide/chapter_base.html` extends it with the common chapter layout. Every chapter then extends `chapter_base.html` and supplies only its hardcoded learning content.

This gives the project both properties requested:

- every chapter remains a real, individually editable HTML template;
- shared interface code is not duplicated.

## Chapters

1. World, Rules and Responsibilities
2. Tkinter and Turtle: The Garden Interface
3. Async, Events and Concurrency
4. Local AI with Ollama and LiteLLM
5. The First Agent, Tools and Safe Execution
6. Memory, Recall and SQLite Persistence
7. Communication Between Agents
8. Contracts, Standards and Reliability
9. Artificial-Life Experiments

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>.

## Tests

```bash
python manage.py test
python manage.py check
```

The tests verify the landing-page brand, all nine explicit chapter routes, their templates and the first/last navigation boundaries.

To generate a static review build from the same Django templates:

```bash
python scripts/export_static.py _site_export
```

## Project structure

```text
in-a-gadda-da-vida/
├── _core/
├── guide/
│   └── templates/guide/
│       ├── chapter_base.html
│       └── chapters/chapter_01.html ... chapter_09.html
├── main/
├── static/
│   ├── css/site.css
│   ├── img/eden-research-lab-v2.webp
│   └── js/site.js
├── templates/
│   ├── base.html
│   └── partials/
├── manage.py
└── requirements.txt
```

## Interface and accessibility

- The document shell keeps navigation, main content, footer and scripts inside `<body>`.
- Layout primitives have explicit full-width and `min-width: 0` safeguards to prevent narrow mobile pages and horizontal overflow.
- Protocol diagrams become vertical connected flows below the tablet breakpoint.
- The architecture map separates decision support from the authority path: model output is a proposal, while validated tools and the simulation engine control world mutations.
- Decorative live-status lights and blinking indicators are intentionally absent; interface labels describe the research instead of making claims about a running service.
- A keyboard skip link, visible focus states and `aria-current` chapter navigation are included.

## Production notes

Static files are served by WhiteNoise with compressed, content-hashed filenames. Settings are loaded from `.env` using `python-dotenv`; environment variables supplied by the deployment platform override that file. `.env` is ignored by Git and `.env.example` is the safe production template. Django refuses to start if `DJANGO_SECRET_KEY` is missing. Before deployment, replace that secret, provide comma-separated hosts through `DJANGO_ALLOWED_HOSTS`, run `collectstatic`, serve through a production WSGI/ASGI server and apply Django's deployment checklist.

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with the deployment secret and hostnames.
python manage.py collectstatic --noinput
python manage.py check --deploy
```

HTTPS redirects, secure cookies, and one-year HSTS (including subdomains and preload) are enabled by default when `DJANGO_DEBUG` is false. If TLS is terminated by a reverse proxy, configure that proxy to pass the original HTTPS protocol and set Django's trusted proxy header configuration for that platform before enabling `DJANGO_SECURE_SSL_REDIRECT`; otherwise it can create a redirect loop. For a first HSTS rollout, set `DJANGO_SECURE_HSTS_SECONDS=0` and `DJANGO_SECURE_HSTS_PRELOAD=false` until HTTPS is confirmed for every host and subdomain.
