from django.shortcuts import render, redirect
from .models import Emprestimo
from .forms import CriarEmprestimoForm, EditarEmprestimoForm
from django.contrib import messages #Para as mensagem de erro e sucesso
from datetime import timedelta #Para a função renovar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound 

# Create your views here.


# Função listar
@login_required
def listar(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo/listar.html', {'emprestimos': emprestimos})

# Função create
@login_required
def criar(request):
    if request.method == 'POST':
        form = CriarEmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_listar')
    else:
        form = CriarEmprestimoForm()
    context = {
        'form': form,
    }
    return render(request, 'emprestimo/criar.html', context)

# Função atualizar
@login_required
def editar(request, emprestimo_id):
    emprestimo = Emprestimo.objects.get(id=emprestimo_id)
    if request.method == 'POST':
        form = EditarEmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_listar')
    else:
        form = EditarEmprestimoForm(instance=emprestimo)
    context = {
        'form': form,
    }
    return render(request, 'emprestimo/editar.html', context)

# Função detalhar
@login_required
def detalhar(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    return render(request, 'emprestimo/ver.html', {'emprestimo': emprestimo})

# Função renovar
@login_required
def renovar(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    if emprestimo.cliente != request.user:
        return HttpResponseNotFound("Emprestimo nao encontrado.")

    if emprestimo.renovado:
        messages.error(request, "Este empréstimo já foi renovado uma vez.")
        return redirect('emprestimo_detalhar', emprestimo_id=emprestimo.id)

    emprestimo.data_prevista_devolucao += timedelta(days=7)
    emprestimo.renovado = True
    emprestimo.save()

    messages.success(request, "Empréstimo renovado com sucesso.")
    return redirect('emprestimo_detalhar', emprestimo_id=emprestimo.id)

# Função concluir (sem apagar, apenas atualizando o status)
@login_required
def concluir(request, emprestimo_id):
    emprestimo = Emprestimo.objects.get(id=emprestimo_id)
    emprestimo.status = 'devolvido'
    emprestimo.save()
    messages.success(request, "Empréstimo concluído com sucesso.")
    return redirect('emprestimo_listar')