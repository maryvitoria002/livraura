from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="emprestimo_index"),
    path("criar/", views.criar, name="emprestimo_criar"),
    path("editar/<int:livro_id>/", views.atualizar, name="emprestimo_editar"),
    path("excluir/<int:livro_id>/", views.excluir, name="emprestimo_excluir"),
    path("ver/<int:livro_id>/", views.ver, name="emprestimo_ver"),
]