from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm


# Criar livro
def criar(request):
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("livro_listar")

    return render(request, "livro/criar.html", {"form": form})


# Listar livro
def listar(request):
    livros = Livro.objects.all()

    # agrupados = dict(list)

    # for livro in livros:
    #     chave = (
    #         livro.titulo,
    #         livro.editora
    #     )
    #     agrupados[chave].append(livro)

    return render(request, "livro/listar.html", {"livros": livros})

# Atualizar livro
def editar(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect("livro_listar")

    return render(request, "livro/editar.html",{"form":form})

# Deletar livro
def deletar(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()

    return redirect("livro_listar")

def detalhar(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    context = {
        'livro': livro,
    }
    return render(request, 'livro/detalhar.html', context)
