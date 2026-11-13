from django.urls import path
from . import views

app_name = "cultura"

urlpatterns = [
    path("", views.home, name="home"),
    path("comunidades/", views.comunidades, name="comunidades"),
    path("comunidades/<int:pk>/", views.comunidade_detalhe, name="comunidade_detalhe"),
    path("eventos/", views.eventos, name="eventos"),
    path("artistas/", views.artistas, name="artistas"),
    path("exposicoes/", views.exposicoes, name="exposicoes"),
]
