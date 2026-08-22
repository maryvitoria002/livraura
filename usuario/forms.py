from django import forms
from django.forms import ModelForm
from .models import Usuario

class CriarUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'cpf', 'username', 'email', 'password']

class EditarUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username',]

