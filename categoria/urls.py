from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="categoria_listar"),
    path("criar/", views.criar, name="categoria_criar"),
    path("editar/<int:categoria_id>/", views.editar, name="categoria_editar"),
    path("deletar/<int:categoria_id>/", views.deletar, name="categoria_deletar"),
    path("detalhar/<int:categoria_id>/", views.detalhar, name="categoria_detalhar"),
]