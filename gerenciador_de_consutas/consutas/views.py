from django.shortcuts import render
from .models import Consuta
from django.contrib import messages
from .forms import ConsutaForm



def index(request):
    consutas = Consuta.objects.all()

    context = {
        'consutas':consutas,
    }

    return render(request, 'consutas/index.html', context) 
 
def cadastro(request):
    if request.method == 'POST':
        form = ConsutaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consuta Agendada!!')
            form = ConsutaForm()

        else:
            messages.error(request, 'Erro Ao Agendar.')
    else:
        form = ConsutaForm()
    
    return render(request, 'consutas/cadastro.html', {'form': form})

