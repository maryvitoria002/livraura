from django.db import models

# Create your models here.

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome