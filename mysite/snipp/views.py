from django.shortcuts import render


def inicial(request):
    return render(request, 'snipp/inicial.html')

def teste(request):
    return render(request, 'snipp/base.html')

def contato(request):
    return render(request, 'snipp/contato.html')

def sobre(request):
    return render(request, 'snipp/sobre.html')

def colaborador(request):
    return render(request, 'snipp/colaborador.html')

def adocao(request):
    return render(request, 'snipp/adocao.html')

def hamster(request):
    return render(request, 'snipp/hamster.html')

def cachorro(request):
    return render(request, 'snipp/cachorro.html')

def service(request):
    return render(request, 'snipp/services.html')



