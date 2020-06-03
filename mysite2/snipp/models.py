from django.db import models
from django import forms

class ModelEmail(models.Model):
    email = models.CharField(max_length=100, null=True)

class Contato(models.Model):
    nome =  models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, null=False, blank=True)
    assunto = models.CharField(max_length=200, blank=True)
    mensagem = models.TextField(null=False,blank=True)
