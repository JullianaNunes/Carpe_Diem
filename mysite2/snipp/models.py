from django.db import models
from django import forms

class ModelEmail(models.Model):
    email = models.CharField(max_length=100, null=True)