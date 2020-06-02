from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicial, name='Inicial'),
    path('snipp/', views.teste, name='Snipp'), 
    path('contato/', views.contato, name='Contato'),
    path('sobre/', views.sobre, name='Sobre'),
    path('colaborador/', views.colaborador, name='Colaborador'),
    path('adocao/', views.adocao, name='Adocao'),
    path('hamster/', views.hamster, name='Hamster'),
    path('cachorro/', views.cachorro, name='Cachorro'),
    path('porquinho/', views.porquinho, name='Porquinho'),
    path('service/', views.service, name='Service'), # Para exemplo
    path('emails/list/', views.lista_colaborador, name='Emails'),
    path('contato/list/', views.lista_contato, name='Lista_contatos')
]