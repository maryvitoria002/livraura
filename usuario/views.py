from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

@login_required
@permission_required('usuario.view_usuario', raise_exception=True) #verifica se o usuário tem permissão para visualizar a lista de usuários

#essa view lista todos os usuários cadastrados no sistema
def usuario_list(request):
    usuarios = Usuario.objects.all() #consulta todos os usuários cadastrados no banco de dados
    return render(request, 'usuario/usuario_list.html', {'usuarios': usuarios})

@login_required
@permission_required('usuario.add_usuario', raise_exception=True) #verifica se o usuário tem permissão para adicionar um novo usuário
#essa view cria um novo usuário no sistema
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/usuario/')
        
    else:
        print("Mostrar formulário para criar nova pessoa")

        form = UsuarioForm()

    return render(request, 'usuario/usuario_form.html', {'form': form})

@login_required
@permission_required('usuario.change_usuario', raise_exception=True) #verifica se o usuário tem permissão para atualizar um usuário existente
#essa view atualiza um usuário existente no sistema
def usuario_update(request, pk):

    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':

        form = UsuarioForm(request.POST, instance=usuario) 

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/usuario/')
    else:
        print("Mostrar formulário para atualizar pessoa existente")

        form = UsuarioForm(instance=usuario)

    return render(request, 'usuario/usuario_form.html', {'form': form})

@login_required
@permission_required('usuario.delete_usuario', raise_exception=True) #verifica se o usuário tem permissão para excluir um usuário
#essa view exclui um usuário no sistema
def usuario_delete(request, pk):
    usuario = Usuario.objects.get(pk=pk) #consulta o usuário no banco de dados

    if request.method == 'POST':
        usuario.delete()

        return HttpResponseRedirect('/usuario/')
    
    return render(request, 'usuario/usuario_confirm_delete.html', {'usuario': usuario})

@login_required
@permission_required('usuario.view_usuario', raise_exception=True)#verifica se o usuário tem permissão para visualizar os detalhes de um usuário
#essa view exibe os detalhes de um usuário no sistema
def usuario_detail(request, pk):
    usuario = Usuario.objects.get(pk=pk) #consulta o usuário no banco de dados

    return render(request, 'usuario/usuario_detail.html', {'usuario': usuario})
