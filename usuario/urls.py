from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='usuario_index'),
    path('criar/', views.criar, name='usuario_criar'),
    path('editar/<int:usuario_id>/', views.editar, name='usuario_editar'),
    path('ver/<int:usuario_id>/', views.ver, name='usuario_ver'),
    path('deletar/<int:usuario_id>/', views.deletar, name='usuario_deletar'),
]