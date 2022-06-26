from .models import City
from django import forms


class CityForm(forms.ModelForm):
    class Meta:
        madel = City
        fields = ['name']

        widgets = {'name': forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'})}