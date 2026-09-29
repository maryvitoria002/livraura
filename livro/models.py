from django.db import models
from editora.models import Editora
from autor.models import Autor
from categoria.models import Categoria

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    disponivel = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros")
    categoria = models.ManyToManyField(Categoria, related_name="livros")
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")

    def __str__(self):
        return self.titulo