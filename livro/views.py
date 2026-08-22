from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm


# Criar livro

def criar(request):
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("livro_index")

    return render(request, "livro/criar.html", {"form":form})

# Listar livro
def index(request):
    livros = Livro.objects.all()
    # agrupados = dict(list)

    # for livro in livros:
    #     chave = (
    #         livro.titulo,
    #         livro.editora
    #     )
    #     agrupados[chave].append(livro)

    return render(request, "livro/index.html", {"livros": livros})

# Atualizar livro
def atualizar(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect("livro_index")

    return render(request, "livro/editar.html",{"form":form})

# Excluir livro
def excluir(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()

    return redirect("livro_index")

def ver(request, livro_id): 
    livro = Livro.objects.get(id=livro_id)
    context = {
        'livro': livro,
    }
    return render(request, 'livro/ver.html', context)