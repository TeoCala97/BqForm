from dataclasses import field
from django import forms
from .models import Form

class Formulario(forms.ModelForm):

    class Meta:
        model = Form
        fields = '__all__'
        widgets = {'fecha':forms.DateTimeInput(attrs={'type': 'date','class':'form-control-sm'})}