from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
import email


def inicial(request):
    return render(request, 'snipp/inicial.html')

def teste(request):
    return render(request, 'snipp/base.html')

def contato(request):
    return render(request, 'snipp/contato.html')
    
def sobre(request):
    return render(request, 'snipp/sobre.html')

def colaborador(request):
    form = Email_save(request.POST)
    if form.is_valid():
        form.save()
        return redirect('snipp/colaborador.html')

    return render(request, 'snipp/colaborador.html', {'form':form})

def lista_colaborador(request):
    
    emails = ModelEmail.objects.all()
    return render(request, 'snipp/email_list.html', {'emails': emails})

def adocao(request):
    return render(request, 'snipp/adocao.html')

def hamster(request):
    return render(request, 'snipp/hamster.html')

def cachorro(request):
    return render(request, 'snipp/cachorro.html')

def porquinho(request):
    return render(request, 'snipp/porquinho.html')

def service(request):
    return render(request, 'snipp/services.html')



