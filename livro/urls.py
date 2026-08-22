from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.listar,
        name="listar_livros"
    ),

    path(
        "criar/",
        views.criar,
        name="criar_livro"
    ),

    path(
        "editar/<int:id>/",
        views.atualizar,
        name="editar_livro"
    ),

    path(
        "excluir/<int:id>/",
        views.excluir,
        name="excluir_livro"
    ),

]