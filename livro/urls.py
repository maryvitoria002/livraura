from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="livro_listar"),
    path("criar/", views.criar, name="livro_criar"),
    path("editar/<int:livro_id>/", views.editar, name="livro_editar"),
    path("deletar/<int:livro_id>/", views.deletar, name="livro_deletar"),
    path("detalhar/<int:livro_id>/", views.detalhar, name="livro_detalhar"),
    path("criar_editora/", views.criar_editora, name="criar_editora"),
    path("listar_editoras/", views.listar_editoras, name="listar_editoras"),
    path("visualizar_editora/<int:id>/", views.visualizar_editora, name="visualizar_editora"),
    path("editar_editora/<int:id>/", views.editar_editora, name="editar_editora"),
    path("excluir_editora/<int:id>/", views.excluir_editora, name="excluir_editora"),
    path("categorias/", views.listar_categorias, name="listar_categorias"),
    path("categoria/criar/", views.criar_categoria, name="criar_categoria"),
    path("categoria/<int:id>/", views.visualizar_categoria, name="visualizar_categoria"),
    path("categoria/<int:id>/editar/", views.atualizar_categoria, name="editar_categoria"),
    path("categoria/<int:id>/excluir/", views.excluir_categoria, name="excluir_categoria"),
    path("criar_autor/", views.criar_autor, name="criar_autor"),
    path("listar_autores/", views.listar_autores, name="listar_autores"),
    path("editar_autor/<int:id>/", views.editar_autor, name="editar_autor"),
    path("excluir_autor/<int:id>/", views.excluir_autor, name="excluir_autor"),
]