from django.db import models

class Consuta(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.FloatField()
    hora = models.TimeField()
    dat_con = models.DateField(auto_now_add=True)

def __init__(self):
    return self.nome 