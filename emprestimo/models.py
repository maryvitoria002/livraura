# Create your models here.
from usuario.models import Usuario
from django.db import models
from livro.models import Livro

class Emprestimo(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='emprestimos_como_cliente')
    bibliotecario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='emprestimos_como_bibliotecario')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='emprestimos_como_livro')
    data_emprestimo = models.DateField()
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Empréstimo feito por {self.cliente.username} com bibliotecário {self.bibliotecario.username} em {self.data_emprestimo}"