from django import forms 
from .models import * 

class CreateDatabaseForm(forms.ModelForm):
    class Meta: 
        model = Database 
        fields = ['name', 'db_type']


class CreateDatabaseFieldForm(forms.ModelForm): 
    class Meta:
        model = DatabaseField 
        fields = ['field_type', 'name', 'description', ]