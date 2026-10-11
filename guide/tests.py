"""Route and template tests for all hardcoded guide chapters."""

from django.test import TestCase
from django.urls import reverse

from .data import CHAPTERS


class ChapterPageTests(TestCase):
    """Ensure every declared protocol has a working English page."""

    def test_all_chapter_pages_render(self):
        for chapter in CHAPTERS:
            with self.subTest(chapter=chapter["number"]):
                response = self.client.get(reverse(chapter["url_name"]))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, chapter["title"])
                self.assertTemplateUsed(
                    response,
                    f"guide/chapters/chapter_{chapter['number']}.html",
                )
                html = response.content.decode()
                self.assertLess(html.index("<body"), html.index('class="chapter-header"'))
                self.assertLess(html.index('class="chapter-header"'), html.index("</body>"))

    def test_first_and_last_chapter_navigation_boundaries(self):
        first = self.client.get(reverse("guide:chapter-01"))
        last = self.client.get(reverse("guide:chapter-09"))

        self.assertNotContains(first, "PREVIOUS PROTOCOL")
        self.assertNotContains(last, "NEXT PROTOCOL")
