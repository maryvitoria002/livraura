from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='usuario_listar'),
    path('criar/', views.criar, name='usuario_criar'),
    path('editar/<int:usuario_id>/', views.editar, name='usuario_editar'),
    path('ver/<int:usuario_id>/', views.detalhar, name='usuario_detalhar'),
    path('deletar/<int:usuario_id>/', views.deletar, name='usuario_deletar'),
    path('login/', views.login_view, name='usuario_login'),
    path('logout/', views.logout_view, name='usuario_logout'),
]