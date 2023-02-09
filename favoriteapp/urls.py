from django.urls import path

import favoriteapp.views as favoriteapp

from .apps import FavoriteappConfig

app_name = FavoriteappConfig.name

urlpatterns = [
    path("candidate/", favoriteapp.favorites_candidate, name="candidate_view"),
    path("company/", favoriteapp.favorites_company, name="company_view"),

    path("candidate/add/<int:pk>/", favoriteapp.favorite_add_candidate, name="candidate_add"),
    path("company/add/<int:pk>/", favoriteapp.favorite_add_company, name="company_add"),

    path("candidate/remove/<int:pk>/", favoriteapp.favorite_remove_candidate, name="candidate_remove"),
    path("company/remove/<int:pk>/", favoriteapp.favorite_remove_company, name="company_remove"),
]
