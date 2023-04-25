from .models import *
from django.forms import ModelForm, TextInput


class client_form(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'telephone', 'mail', 'client_city']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Введите имя'
            }),
            'telephone': TextInput(attrs={
                'placeholder': 'Введите телефон',
            }),
            'mail': TextInput(attrs={
                'placeholder': 'Введите почту',
            }),
            'client_city': TextInput(attrs={
                'placeholder': 'Введите ваш город',
            })
        }
