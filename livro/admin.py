from django.contrib import admin
from .models import Autor, Categoria, Editora, Livro

# Register your models here.

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)