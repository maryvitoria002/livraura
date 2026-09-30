from django.contrib.auth.models import Group
from django import forms
from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CriarUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = [ 'cpf', 'username', 'email']

    def save (self, commit=True):
        usuario = super().save(commit=False)
        grupo_cliente, _ = Group.objects.get_or_create(name='cliente')
        if commit:
            usuario.save()
            self.save_m2m()
            usuario.groups.add(grupo_cliente)
        return usuario
    
class EditarUsuarioForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ['username',]

