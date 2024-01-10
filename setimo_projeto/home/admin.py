from django.contrib import admin
from .models import Produto

class ListProduto(admin.ModelAdmin):
    list_display = ('nome_produto', 'descricao', 'categoria', 'preco')

admin.site.register(Produto, ListProduto)
