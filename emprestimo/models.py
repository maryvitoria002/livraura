# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from livro.models import Livro

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprestimos_como_cliente')
    bibliotecario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprestimos_como_bibliotecario')

    data_emprestimo = models.DateField()
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pendente')
    renovado = models.BooleanField(default=False) #se tiver true ent nao vai dar pra renovar mais, só pode 1 vez
    
    def __str__(self):
        return f"Empréstimo feito por {self.cliente.username} com bibliotecário {self.bibliotecario.username} em {self.data_emprestimo}"