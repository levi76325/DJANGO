from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def home(request):
    meus_produtos = Produto.objects.all()

    context = {
        'produtos': meus_produtos, 

    }

    return render(request, 'home/index.html', context)
