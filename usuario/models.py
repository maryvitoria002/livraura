from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(User):
    cpf = models.CharField(max_length=15, blank=False, null=False, unique=True)

    def __str__(self):
        return self.username