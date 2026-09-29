def usuario_context(request):
    eh_cliente = request.user.is_authenticated and request.user.groups.filter(name='cliente').exists()
    return {'eh_cliente': eh_cliente}
