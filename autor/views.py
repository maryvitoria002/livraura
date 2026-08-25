from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm

def criar(request):
    form = AutorForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("autor_listar")
    
    return render(request, "autor/criar.html", {"form": form})

def listar(request):
    autores = Autor.objects.all()
    return render(request, "autor/listar.html", {"autores": autores})

def detalhar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    return render(request, "autor/detalhar.html", {"autor": autor})

def editar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)

    if form.is_valid():
        form.save()
        return redirect("autor_listar")
    
    return render(request, "autor/editar.html",{"form":form})

def deletar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.delete()
    return redirect("autor_listar")