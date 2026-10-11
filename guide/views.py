"""Explicit views for the nine hardcoded chapter templates."""

from django.shortcuts import render

from .data import chapter_context


def _chapter(request, number: str):
    """Render one hardcoded template while sharing navigation metadata."""
    return render(request, f"guide/chapters/chapter_{number}.html", chapter_context(number))


def chapter_01(request):
    return _chapter(request, "01")


def chapter_02(request):
    return _chapter(request, "02")


def chapter_03(request):
    return _chapter(request, "03")


def chapter_04(request):
    return _chapter(request, "04")


def chapter_05(request):
    return _chapter(request, "05")


def chapter_06(request):
    return _chapter(request, "06")


def chapter_07(request):
    return _chapter(request, "07")


def chapter_08(request):
    return _chapter(request, "08")


def chapter_09(request):
    return _chapter(request, "09")
