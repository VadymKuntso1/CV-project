from .models import User
from django.forms import ModelForm,TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login','password']
        widgets = {
            'login': TextInput(attrs={'class':'form-control'}),
            'password': TextInput(attrs={'class':'form-control'})

        }