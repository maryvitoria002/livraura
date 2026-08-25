from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome