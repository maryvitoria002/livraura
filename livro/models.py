from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True)
    disponivel = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    editora = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo