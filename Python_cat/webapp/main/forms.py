from .models import *
from django.forms import ModelForm, TextInput, NumberInput, DateInput


class client_form(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'age', 'birth_date', 'mail']

        widgets = {
            'name': TextInput(attrs={
                'class': '=color: #FFFFFF',
                'placeholder': 'Введите имя'
            }),
            'age': NumberInput(attrs={
                'class': '',
                'placeholder': 'Введите возраст'
            }),
            'birt_date': DateInput(attrs={
                'class': '',
                'placeholder': 'Введите дату рождения'  # не работкает
            }),
            'mail': TextInput(attrs={
                'class': '',
                'placeholder': 'Введите почту'
            })}
