from django.urls import path

from scraping.views import index

urlpatterns = [
    path("", index, name="index"),
]
