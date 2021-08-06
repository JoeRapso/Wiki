from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("createPage", views.createPage, name="createPage"),
    path("createdPage", views.createdPage, name="createdPage"),
    path("editPage", views.editPage, name="editPage"),
    path("editedPage", views.editedPage, name="editedPage"),
    path("randomPage", views.randomPage, name="randomPage")
]