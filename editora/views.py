from django.shortcuts import render, redirect, get_object_or_404
from .models import Editora

def criar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        editora = Editora(nome=nome)
        editora.save()
        return redirect("editora_listar")

    return render(request, "editora/criar.html")

def listar(request):
    editoras = Editora.objects.all()
    return render(request, "editora/listar.html", {"editoras": editoras})

def detalhar(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    return render(request, "editora/detalhar.html", {"editora": editora})

def editar(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)

    if request.method == "POST":
        nome = request.POST.get("nome")
        editora.nome = nome
        editora.save()
        return redirect("editora_listar")

    return render(request, "editora/editar.html", {"editora": editora})

def deletar(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    editora.delete()
    return redirect("editora_listar")