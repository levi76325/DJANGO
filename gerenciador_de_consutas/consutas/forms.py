from django import forms
from .models import Consuta

class ConsutaForm(forms.ModelForm):
    class Meta:
        model = Consuta
        fields = '__all__'