from django import forms 
from .models import * 

class CreateWorkspaceForm(forms.ModelForm): 
    class Meta: 
        model = Workspace 
        fields = ['name', ]


class CreateWebsiteForm(forms.ModelForm): 
    class Meta: 
        model = Website  
        fields = ['name', 'ui']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "ادخل اسم الموقع"}), 
            'ui': forms.FileInput(attrs={'accept': '.zip,.rar'})
        }


class CreateWebsitePageForm(forms.ModelForm):

    class Meta:
        model = WebsitePage
        fields = ('name',)
