from django import forms
from .models import *

class Email_save(forms.ModelForm):
    class Meta:
        model = ModelEmail
        fields = ('email',)  

class Contato_save(forms.ModelForm):
    class Meta: 
        model = Contato
        fields = ('nome', 'email', 'assunto', 'mensagem')
        email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))