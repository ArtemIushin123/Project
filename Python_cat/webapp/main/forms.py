from .models import *
from django.forms import ModelForm, TextInput, NumberInput, DateInput, EmailInput


class client_form(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'telephone', 'mail']

        widgets = {
            'name': TextInput(attrs={
                'class': '=color: #FFFFFF',
                'placeholder': 'Введите имя'
            }),
            'telephone': TextInput(attrs={
                'class': '',
                'placeholder': 'Введите номер телефона'
            }),
            'mail': EmailInput(attrs={
                'class': '',
                'placeholder': 'Введите почту'
            })}
