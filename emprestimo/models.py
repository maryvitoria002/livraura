# Create your models here.
from .models import Usuario
from django.db import models

class Emprestimo(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_como_cliente')
    bibliotecario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_como_bibliotecario')
    data_emprestimo = models.DateField()
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Empréstimo feito por {self.cliente.username} com bibliotecário {self.bibliotecario.username} em {self.data_emprestimo}"