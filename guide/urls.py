from django.urls import path

from . import views

app_name = "guide"

urlpatterns = [
    path("01/world-rules-responsibilities/", views.chapter_01, name="chapter-01"),
    path("02/tkinter-turtle-interface/", views.chapter_02, name="chapter-02"),
    path("03/async-events-concurrency/", views.chapter_03, name="chapter-03"),
    path("04/ollama-litellm/", views.chapter_04, name="chapter-04"),
    path("05/agent-tools-safe-execution/", views.chapter_05, name="chapter-05"),
    path("06/memory-sqlite/", views.chapter_06, name="chapter-06"),
    path("07/agent-communication/", views.chapter_07, name="chapter-07"),
    path("08/contracts-reliability/", views.chapter_08, name="chapter-08"),
    path("09/experiments-simulation/", views.chapter_09, name="chapter-09"),
]
