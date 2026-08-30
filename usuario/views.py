from django.shortcuts import render, redirect
from .models import Usuario
from .forms import CriarUsuarioForm, EditarUsuarioForm
from  django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
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

@login_required
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
@login_required
def deletar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect('usuario_listar')

@login_required
# Função read
def detalhar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    context = {
        'usuario': usuario,
    }
    return render(request, 'usuario/detalhar.html', context)

#Função login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redireciona para a página de destino após o login bem-sucedido
            next = request.GET.get('next') or "usuario_listar"
            return redirect(next)
        else:
            error_message = 'Nome de usuário ou senha inválidos.'
            # Caso de erro, renderiza o formulário de login novamente com a mensagem de erro
            form = AuthenticationForm(data=request.POST)
            return render(request, 'usuario/login.html', {'error_message': error_message, 'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'usuario/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('usuario_login')