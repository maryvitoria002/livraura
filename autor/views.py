from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm
from django.contrib.auth.decorators import login_required

@login_required
def criar(request):
    form = AutorForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("autor_listar")
    
    return render(request, "autor/criar.html", {"form": form})

@login_required
def listar(request):
    autores = Autor.objects.all()
    return render(request, "autor/listar.html", {"autores": autores})

@login_required
def detalhar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    return render(request, "autor/detalhar.html", {"autor": autor})

@login_required
def editar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)

    if form.is_valid():
        form.save()
        return redirect("autor_listar")
    
    return render(request, "autor/editar.html",{"form":form})

@login_required
def deletar(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.delete()
    return redirect("autor_listar")

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