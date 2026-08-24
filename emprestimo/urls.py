from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="emprestimo_listar"),
    path("criar/", views.criar, name="emprestimo_criar"),
    path("editar/<int:emprestimo_id>/", views.editar, name="emprestimo_editar"),
    path("ver/<int:emprestimo_id>/", views.detalhar, name="emprestimo_detalhar"),
    path("renovar/<int:emprestimo_id>/", views.renovar, name="emprestimo_renovar"),
    path("concluir/<int:emprestimo_id>/", views.concluir, name="emprestimo_concluir"),
]