from django.shortcuts import render, redirect
from .models import Usuario
from .forms import CriarUsuarioForm, EditarUsuarioForm

# Create your views here.

def listar(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar.html', {'usuarios': usuarios})

# Função create
def criar(request):
    if request.method == 'POST':
        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_listar')
    else:
        form = CriarUsuarioForm()
    context = {
        'form': form,
    }
    return render(request, 'usuario/criar.html', context)

# Função update
def editar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_listar')
    else:
        form = EditarUsuarioForm(instance=usuario)
    context = {
        'form': form,
    }
    return render(request, 'usuario/editar.html', context)

# Função delete
def deletar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect('usuario_listar')

# Função read
def detalhar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    context = {
        'usuario': usuario,
    }
    return render(request, 'usuario/ver.html', context)