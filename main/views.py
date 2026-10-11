"""Views for the presentation layer of the guide."""

from django.shortcuts import render


def home(request):
    """Render the project landing page."""
    return render(request, "main/home.html")
