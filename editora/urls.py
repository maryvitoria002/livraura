from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="editora_listar"),
    path("criar/", views.criar, name="editora_criar"),
    path("editar/<int:editora_id>/", views.editar, name="editora_editar"),
    path("deletar/<int:editora_id>/", views.deletar, name="editora_deletar"),
    path("detalhar/<int:editora_id>/", views.detalhar, name="editora_detalhar"),
]
