from django.shortcuts import render, redirect, get_object_or_404
from .models import Editora
from .forms import EditoraForm

def criar(request):
    form = EditoraForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("editora_listar")
    
    return render(request, "editora/criar.html", {"form": form})

def listar(request):
    editoras = Editora.objects.all()
    return render(request, "editora/listar.html", {"editoras": editoras})

def detalhar(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    return render(request, "editora/detalhar.html", {"editora": editora})

def editar(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    form = EditoraForm(request.POST or None, instance=editora)

    if form.is_valid():
        form.save()
        return redirect("editora_listar")
    
    return render(request, "editora/editar.html",{"form":form})

def deletar(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    editora.delete()
    return redirect("editora_listar")