from .models import Table
from django.forms import ModelForm, TextInput

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            })
        }