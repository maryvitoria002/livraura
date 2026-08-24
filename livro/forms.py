from django import forms
from .models import Livro, Autor, Categoria, Editora


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro

        fields = [
            "titulo",
            "descricao",
            "autor",
            "categoria",
            "editora"
        ]

class EditoraForm(forms.ModelForm):

    class Meta:
        model = Editora
        fields = [
            "nome",
            "cnpj"
        ]

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            "nome",
            "descricao"
        ]

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor

        fields = [
            "nome",
            "biografia"
        ]