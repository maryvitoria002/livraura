from django.shortcuts import render, redirect
from .models import Emprestimo
from .forms import CriarEmprestimoForm, EditarEmprestimoForm
from django.contrib import messages #Para as mensagem de erro e sucesso
from datetime import timedelta #Para a função renovar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseNotFound 
from django.utils import timezone

# Create your views here.


# Função listar
@login_required
@permission_required("emprestimo.view_emprestimo")
def listar(request):
    if request.user.has_perm('emprestimo.change_emprestimo'):
        emprestimos = Emprestimo.objects.all()
    else:
        emprestimos = Emprestimo.objects.filter(cliente_id=request.user.pk)
    return render(request, 'emprestimo/listar.html', {'emprestimos': emprestimos})

# Função create
@login_required
@permission_required("emprestimo.add_emprestimo")
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
@permission_required("emprestimo.change_emprestimo")
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
@permission_required("emprestimo.view_emprestimo")
def detalhar(request, emprestimo_id):
    if request.user.has_perm('emprestimo.change_emprestimo'):
        emprestimos = Emprestimo.objects.all()
    else:
        emprestimos = Emprestimo.objects.filter(cliente_id=request.user.pk)
    emprestimo = get_object_or_404(emprestimos, id=emprestimo_id)
    return render(request, 'emprestimo/detalhar.html', {'emprestimo': emprestimo})

# Função renovar
@login_required
def renovar(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    pode_renovar = (
        emprestimo.cliente_id == request.user.pk
        or request.user.has_perm('emprestimo.change_emprestimo')
    )
    if not pode_renovar:
        return HttpResponseNotFound("Emprestimo nao encontrado.")

    if emprestimo.renovado or emprestimo.status == 'devolvido':
        messages.error(request, "Este empréstimo já foi renovado uma vez.")
        return redirect('emprestimo_detalhar', emprestimo_id=emprestimo.id)

    emprestimo.data_prevista_devolucao += timedelta(days=7)
    emprestimo.renovado = True
    emprestimo.save()

    messages.success(request, "Empréstimo renovado com sucesso.")
    return redirect('emprestimo_detalhar', emprestimo_id=emprestimo.id)

# Função concluir (sem apagar, apenas atualizando o status)
@login_required
@permission_required("emprestimo.change_emprestimo")
def concluir(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    emprestimo.status = 'devolvido'
    emprestimo.data_devolucao = timezone.localdate()
    emprestimo.save()
    messages.success(request, "Empréstimo concluído com sucesso.")
    return redirect('emprestimo_listar')
