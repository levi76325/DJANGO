from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    descricao = models.TextField(max_length=350)
    categoria = models.CharField(max_length=60)
    preco = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome_produto
