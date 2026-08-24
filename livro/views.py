from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Editora, Categoria, Autor
from .forms import LivroForm, EditoraForm, CategoriaForm, AutorForm


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


# Criar editora
def criar_editora(request):

    form = EditoraForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            "listar_editoras"
        )

    return render(
        request,
        "livros/editora/criar.html",
        {
            "form": form
        }
    )

def listar_editoras(request):

    editoras = Editora.objects.all()


    return render(
        request,
        "livros/editora/listar.html",
        {
            "editoras": editoras
        }
    )

def visualizar_editora(request, id):

    editora = get_object_or_404(
        Editora,
        id=id
    )


    return render(
        request,
        "livros/editora/visualizar.html",
        {
            "editora": editora
        }
    )

def editar_editora(request, id):

    editora = get_object_or_404(
        Editora,
        id=id
    )


    form = EditoraForm(
        request.POST or None,
        instance=editora
    )


    if form.is_valid():

        form.save()

        return redirect(
            "listar_editoras"
        )


    return render(
        request,
        "livros/editora/editar.html",
        {
            "form": form
        }
    )

def excluir_editora(request, id):

    editora = get_object_or_404(
        Editora,
        id=id
    )

    if request.method == "POST":

        editora.delete()

        return redirect(
            "listar_editoras"
        )

    return render(
        request,
        "livros/editora/excluir.html",
        {
            "editora": editora
        }
    )

def criar_categoria(request):

    form = CategoriaForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            "listar_categorias"
        )

    return render(
        request,
        "livro/categoria/criar.html",
        {
            "form": form
        }
    )

def listar_categorias(request):

    categorias = Categoria.objects.all()

    return render(
        request,
        "livro/categoria/listar.html",
        {
            "categorias": categorias
        }
    )

def visualizar_categoria(request, id):

    categoria = get_object_or_404(
        Categoria,
        id=id
    )

    return render(
        request,
        "livro/categoria/visualizar.html",
        {
            "categoria": categoria
        }
    )

def atualizar_categoria(request, id):

    categoria = get_object_or_404(
        Categoria,
        id=id
    )

    form = CategoriaForm(
        request.POST or None,
        instance=categoria
    )


    if form.is_valid():

        form.save()

        return redirect(
            "listar_categorias"
        )


    return render(
        request,
        "livro/categoria/editar.html",
        {
            "form": form
        }
    )


def excluir_categoria(request, id):

    categoria = get_object_or_404(
        Categoria,
        id=id
    )


    if request.method == "POST":

        categoria.delete()

        return redirect(
            "listar_categorias"
        )


    return render(
        request,
        "livro/categoria/excluir.html",
        {
            "categoria": categoria
        }
    )

# Criar autor
def criar_autor(request):

    form = AutorForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            "listar_autores"
        )


    return render(
        request,
        "livros/autor/criar.html",
        {
            "form": form
        }
    )

# Listar autores

def listar_autores(request):

    autores = Autor.objects.all()

    return render(
        request,
        "livros/autor/listar.html",
        {
            "autores": autores
        }
    )

# Editar autor

def editar_autor(request, id):

    autor = get_object_or_404(
        Autor,
        id=id
    )


    form = AutorForm(
        request.POST or None,
        instance=autor
    )


    if form.is_valid():

        form.save()

        return redirect(
            "listar_autores"
        )


    return render(
        request,
        "livros/autor/editar.html",
        {
            "form":form
        }
    )

# Deletar autor
def excluir_autor(request, id):

    autor = get_object_or_404(
        Autor,
        id=id
    )

    autor.delete()

    return redirect(
        "listar_autores"
    )