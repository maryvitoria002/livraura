from django import forms
from django.forms import ModelForm
from .models import Emprestimo

class CriarEmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'cliente', 'bibliotecario', 'data_emprestimo','data_prevista_devolucao','data_devolucao']

class EditarEmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'cliente', 'bibliotecario', 'data_emprestimo','data_prevista_devolucao','data_devolucao']
