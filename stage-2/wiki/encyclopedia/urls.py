from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("wiki/", views.index, name="index"),
    path("wiki/random", views.random, name="random"),
    path("wiki/<str:page>", views.page, name="page"),
    path("editor/<str:title>", views.editor, name="editor")
]