from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="livro_listar"),
    path("criar/", views.criar, name="livro_criar"),
    path("editar/<int:livro_id>/", views.editar, name="livro_editar"),
    path("deletar/<int:livro_id>/", views.deletar, name="livro_deletar"),
    path("detalhar/<int:livro_id>/", views.detalhar, name="livro_detalhar"),
]