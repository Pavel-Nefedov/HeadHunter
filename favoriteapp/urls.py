from django.urls import path

import favoriteapp.views as favoriteapp

from .apps import FavoriteappConfig

app_name = FavoriteappConfig.name

urlpatterns = [
    path("", favoriteapp.favorites, name="view"),
    path("add/<int:pk>/", favoriteapp.favorite_add, name="add"),
    path("remove/<int:pk>/", favoriteapp.favorite_remove, name="remove"),
]
