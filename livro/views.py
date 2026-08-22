from collections import defaultdict

from django.shortcuts import render, redirect, get_object_or_404

from .models import Livro
from .forms import LivroForm


# Criar livro

def criar(request):

    form = LivroForm(
        request.POST or None
    )


    if form.is_valid():

        form.save()

        return redirect(
            "listar_livros"
        )


    return render(
        request,
        "livros/criar.html",
        {
            "form":form
        }
    )



# Listar livro

def listar(request):

    livros = Livro.objects.all()


    agrupados = defaultdict(list)


    for livro in livros:

        chave = (
            livro.titulo,
            livro.editora
        )

        agrupados[chave].append(livro)



    return render(
        request,
        "livros/listar.html",
        {
            "livros": agrupados
        }
    )



# Atualizar livro

def atualizar(request,id):

    livro = get_object_or_404(
        Livro,
        id=id
    )


    form = LivroForm(
        request.POST or None,
        instance=livro
    )


    if form.is_valid():

        form.save()

        return redirect(
            "listar_livros"
        )


    return render(
        request,
        "livros/editar.html",
        {
            "form":form
        }
    )



# Excluir livro

def excluir(request,id):

    livro = get_object_or_404(
        Livro,
        id=id
    )


    livro.delete()


    return redirect(
        "listar_livros"
    )