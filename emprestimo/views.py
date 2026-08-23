from django.shortcuts import render, redirect
from .models import Emprestimo
from .forms import CriarEmprestimoForm, EditarEmprestimoForm

# Create your views here.


# Função listar
def index(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo/index.html', {'emprestimos': emprestimos})

# Função create
def criar(request):
    if request.method == 'POST':
        form = CriarEmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_index')
    else:
        form = CriarEmprestimoForm()
    context = {
        'form': form,
    }
    return render(request, 'emprestimo/criar.html', context)

# Função atualizar
def editar(request, emprestimo_id):
    emprestimo = Emprestimo.objects.get(id=emprestimo_id)
    if request.method == 'POST':
        form = EditarEmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_index')
    else:
        form = EditarEmprestimoForm(instance=emprestimo)
    context = {
        'form': form,
    }
    return render(request, 'emprestimo/editar.html', context)

# Função detalhar
def ver(request, emprestimo_id): 
    emprestimo = Emprestimo.objects.get(id=emprestimo_id)
    context = {
        'emprestimo': emprestimo,
    }
    return render(request, 'emprestimo/ver.html', context)

# Função renovar
def renovar(request, emprestimo_id):
    emprestimo = Emprestimo.objects.get(id=emprestimo_id)
    if request.method == 'POST':
        form = EditarEmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_index')
    else:
        form = EditarEmprestimoForm(instance=emprestimo)
    context = {
        'form': form,
    }
    return render(request, 'emprestimo/renovar.html', context)

# Função concluir (sem apagar, apenas atualizando o status)
def concluir(request, emprestimo_id):
    emprestimo = Emprestimo.objects.get(id=emprestimo_id)
    emprestimo.status = 'concluido'
    emprestimo.save()
    return redirect('emprestimo_index')