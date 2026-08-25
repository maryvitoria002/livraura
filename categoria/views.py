from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm

def criar(request):
    form = CategoriaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("categoria_listar")
    
    return render(request, "categoria/criar.html", {"form": form})

def listar(request):
    categorias = Categoria.objects.all()
    return render(request, "categoria/listar.html", {"categorias": categorias})

def detalhar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, "categoria/detalhar.html", {"categoria": categoria})

def editar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect("categoria_listar")
    
    return render(request, "categoria/editar.html",{"form":form})

def deletar(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect("categoria_listar")