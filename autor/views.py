from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required("autor.add_autor")
def criar(request):
    form = AutorForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("autor_listar")
    
    return render(request, "autor/criar.html", {"form": form})

@login_required
@permission_required("autor.view_autor")
def listar(request):
    autores = Autor.objects.all()
    return render(request, "autor/listar.html", {"autores": autores})

@login_required
@permission_required("autor.view_autor")
def detalhar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    return render(request, "autor/detalhar.html", {"autor": autor})

@login_required
@permission_required("autor.change_autor")
def editar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)

    if form.is_valid():
        form.save()
        return redirect("autor_listar")
    
    return render(request, "autor/editar.html",{"form":form})

@login_required
@permission_required("autor.delete_autor")
def deletar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.delete()
    return redirect("autor_listar")

