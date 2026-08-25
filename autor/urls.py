from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="autor_listar"),
    path("criar/", views.criar, name="autor_criar"),
    path("editar/<int:autor_id>/", views.editar, name="autor_editar"),
    path("deletar/<int:autor_id>/", views.deletar, name="autor_deletar"),
    path("detalhar/<int:autor_id>/", views.detalhar, name="autor_detalhar"),
]