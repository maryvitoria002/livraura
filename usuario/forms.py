from django import forms
from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CriarUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = [ 'cpf', 'username', 'email']

class EditarUsuarioForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ['username',]

