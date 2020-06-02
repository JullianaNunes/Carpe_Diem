from django.shortcuts import redirect, render
from .models import *
from .forms import *


def inicial(request):
    return render(request, 'snipp/inicial.html')

def teste(request):
    return render(request, 'snipp/base.html')

def contato(request):
    return render(request, 'snipp/contato.html')

def sobre(request):
    return render(request, 'snipp/sobre.html')

def colaborador(request):
    form = Email_save(request.GET)
    if form.is_valid():
        form.save()
        return redirect('snipp/colaborador.html')
    return render(request, 'snipp/colaborador.html', {'form':form})

def lista_colaborador(request):
    
    emails = ModelEmail.objects.all()
    
    return render(request, 'snipp/email_list.html', {'emails': emails})
    import pdb; pdb.set_trace()

def adocao(request):
    return render(request, 'snipp/adocao.html')

def hamster(request):
    return render(request, 'snipp/hamster.html')

def cachorro(request):
    return render(request, 'snipp/cachorro.html')

def porquinho(request):
    return render(request, 'snipp/cachorro.html')


def service(request):
    return render(request, 'snipp/services.html')



