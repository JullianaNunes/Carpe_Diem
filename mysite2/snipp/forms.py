from django import forms
from .models import *

class Email_save(forms.ModelForm):
    class Meta:
        model = ModelEmail
        fields = ('email',)  
