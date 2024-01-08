from django.db import models

class Cliente(models.model):
    nome = models.CharField('Nome', max_lenght=30)
    sobrenome = models.CharField('Sobrenome', max_lenght=30)