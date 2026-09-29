from django import forms
from django.forms import ModelForm
from django.db.models import Q
from .models import Emprestimo
from livro.models import Livro
from usuario.models import Usuario


def bibliotecarios_queryset():
    return Usuario.objects.filter(
        Q(groups__name='bibliotecario') | Q(is_staff=True) | Q(is_superuser=True)
    ).distinct()


def clientes_queryset():
    return Usuario.objects.filter(groups__name='cliente').distinct()


def livros_disponiveis_queryset():
    livros_emprestados = Emprestimo.objects.filter(
        data_devolucao__isnull=True
    ).exclude(status='devolvido').values('livro_id')
    return Livro.objects.exclude(id__in=livros_emprestados)


def validar_livro_disponivel(form):
    livro = form.cleaned_data.get('livro')
    if not livro:
        return

    emprestimos_ativos = Emprestimo.objects.filter(
        livro=livro,
        data_devolucao__isnull=True,
    ).exclude(status='devolvido')
    if form.instance.pk:
        emprestimos_ativos = emprestimos_ativos.exclude(pk=form.instance.pk)
    if emprestimos_ativos.exists():
        raise forms.ValidationError('Este livro já está emprestado.')


class CriarEmprestimoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['livro'].queryset = livros_disponiveis_queryset()
        self.fields['cliente'].queryset = clientes_queryset()
        self.fields['bibliotecario'].queryset = bibliotecarios_queryset()

    def clean(self):
        cleaned_data = super().clean()
        validar_livro_disponivel(self)
        return cleaned_data

    class Meta:
        model = Emprestimo
        fields = ['livro', 'cliente', 'bibliotecario', 'data_emprestimo','data_prevista_devolucao','data_devolucao']

class EditarEmprestimoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        livros_disponiveis = livros_disponiveis_queryset()
        if self.instance.pk and self.instance.livro_id:
            livros_disponiveis = Livro.objects.filter(
                Q(id=self.instance.livro_id) | Q(id__in=livros_disponiveis.values('id'))
            )
        self.fields['livro'].queryset = livros_disponiveis
        self.fields['cliente'].queryset = clientes_queryset()
        self.fields['bibliotecario'].queryset = bibliotecarios_queryset()

    def clean(self):
        cleaned_data = super().clean()
        validar_livro_disponivel(self)
        return cleaned_data

    class Meta:
        model = Emprestimo
        fields = ['livro', 'cliente', 'bibliotecario', 'data_emprestimo','data_prevista_devolucao','data_devolucao']
