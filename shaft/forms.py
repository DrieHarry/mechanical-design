from django import forms
from .models import *


class MyForm(forms.Form):
    N = forms.FloatField(label="Faktor Keamanan ",
                            widget=forms.NumberInput(attrs={'value': '2.0', 'min': '0'}))
    P = forms.FloatField(label="Daya ",
                            widget=forms.NumberInput(attrs={'placeholder': 'kW', 'min': '0'}))
    n = forms.FloatField(label="Kecepatan Putar ",
                            widget=forms.NumberInput(attrs={'placeholder': 'rpm', 'min': '0'}))
    Material = forms.ModelChoiceField(
                            label = "Pilih Bahan :", queryset = Materials.objects.all())
    Ft = forms.FloatField(label="Gaya Tangensial Pada Elemen (Ft) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}))
    Fr = forms.FloatField(label="Gaya Radial Pada Elemen (Fr) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}))
    AB = forms.FloatField(label="Jarak Antara Bantalan A ke Elemen B (AB) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0'}))
    BC = forms.FloatField(label="Jarak Antara Bantalan C ke Elemen B (BC) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0'}))

