from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="livro_listar"),
    path("criar/", views.criar, name="livro_criar"),
    path("editar/<int:livro_id>/", views.atualizar, name="livro_editar"),
    path("excluir/<int:livro_id>/", views.excluir, name="livro_excluir"),
    path("ver/<int:livro_id>/", views.ver, name="livro_ver"),
]