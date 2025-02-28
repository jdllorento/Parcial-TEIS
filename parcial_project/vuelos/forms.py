from django import forms
from .models import flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = flight
        fields = ['nombre', 'tipo', 'precio']