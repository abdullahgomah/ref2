from django import forms 
from .models import * 

class CreateDatabaseForm(forms.ModelForm):
    class Meta: 
        model = Database 
        fields = ['name', ]