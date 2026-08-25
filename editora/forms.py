from django import forms
from .models import Editora


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora

        fields = [
            "nome",
            "cnpj",
        ]