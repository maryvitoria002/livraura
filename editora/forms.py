from django import forms
from .models import Editora


class LivroForm(forms.ModelForm):
    class Meta:
        model = Editora

        fields = [
            "nome",
            "cnpj",
        ]