"""Tests for the landing page."""

from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    """Protect the English landing-page contract."""

    def test_home_page_uses_project_brand(self):
        response = self.client.get(reverse("main:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project In-A-Gadda-Da-Vida")
        self.assertContains(response, "Nine protocols")

    def test_home_page_has_documented_workflow_without_fake_live_status(self):
        response = self.client.get(reverse("main:home"))
        html = response.content.decode()

        self.assertContains(response, 'id="workflow"')
        self.assertContains(response, 'class="architecture-map')
        self.assertNotIn("pulse-dot", html)
        self.assertNotIn("OPERATIONAL", html)

    def test_visible_shell_is_inside_body(self):
        html = self.client.get(reverse("main:home")).content.decode()
        body_start = html.index("<body")
        body_end = html.index("</body>")

        for marker in ('class="site-header"', 'id="main-content"', 'class="site-footer"'):
            with self.subTest(marker=marker):
                self.assertLess(body_start, html.index(marker))
                self.assertLess(html.index(marker), body_end)
