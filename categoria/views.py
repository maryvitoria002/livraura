from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm
from  django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required("categoria.add_categoria")
def criar(request):
    form = CategoriaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("categoria_listar")
    
    return render(request, "categoria/criar.html", {"form": form})

@login_required
@permission_required("categoria.view_categoria")
def listar(request):
    categorias = Categoria.objects.all()
    return render(request, "categoria/listar.html", {"categorias": categorias})

@login_required
@permission_required("categoria.view_categoria")
def detalhar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, "categoria/detalhar.html", {"categoria": categoria})

@login_required
@permission_required("categoria.change_categoria")
def editar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect("categoria_listar")
    
    return render(request, "categoria/editar.html",{"form":form})

@login_required
@permission_required("categoria.delete_categoria")
def deletar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect("categoria_listar")
