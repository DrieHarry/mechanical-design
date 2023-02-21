from django import forms
from .models import *


class MyForm(forms.Form):
    N = forms.FloatField(label="Faktor Keamanan ",
                            widget=forms.NumberInput(attrs={'value': '2.0', 'min': '0'}))
    T = forms.FloatField(label="Momen Puntir / Torsi ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N-mm', 'min': '0'}))
    Material = forms.ModelChoiceField(
                            label = "Pilih Bahan :", queryset = Materials.objects.all())
    Sy = forms.FloatField(label="Tegangan Luluh Bahan ",
                            widget=forms.NumberInput(attrs={'placeholder': 'MPa', 'min': '0'}))
    Sn = forms.FloatField(label="Tegangan / Kekuatan Lelah Aktual ",
                            widget=forms.NumberInput(attrs={'placeholder': 'MPa', 'min': '0'}))
    Ft = forms.FloatField(label="Gaya Tangensial Pada Elemen (Ft) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}))
    Fr = forms.FloatField(label="Gaya Radial Pada Elemen (Fr) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}))
    AB = forms.FloatField(label="Jarak Antara Bantalan A ke Elemen B (AB) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0'}))
    BC = forms.FloatField(label="Jarak Antara Bantalan C ke Elemen B (BC) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0'}))

