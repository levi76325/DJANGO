from django.shortcuts import render
from django.contrib import messages
from .forms import FilmeForm
from .models import Filme

def index(request):
    filmes = Filme.objects.all()

    context = {
        'filmes':filmes,

    }
    return render(request, 'cat_filmes/index.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme Salvo!!')
            form = FilmeForm()
        else:
            messages.error(request, 'Erro ao Salvar o Filme!')
    else:
        form = FilmeForm()
    
    return render(request, 'cat_filmes/cadastro.html', {'form': form})
