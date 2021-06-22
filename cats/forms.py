from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Description_of_the_cat


class KockaModelForm(ModelForm):
    def clean_vek(self):
       data = self.cleaned_data['vek']
       if data != None and data <= 0:
           raise ValidationError('Neplatný věk')
       return data

    def clean_rate(self):
       data = self.cleaned_data['vaha']
       if data != None and data < 0:
           raise ValidationError('Neplatná váha')
       return data

    class Meta:
        model = Description_of_the_cat
        fields = ['jmeno', 'vek', 'vaha', 'popisek', 'druh', 'foto']