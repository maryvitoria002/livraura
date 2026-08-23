from django import forms
from django.forms import ModelForm
from .models import Emprestimo

class CriarEmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'cliente', 'data_emprestimo', 'data_devolucao', 'bibliotecario']

class EditarEmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'cliente', 'data_emprestimo', 'data_devolucao', 'bibliotecario']

