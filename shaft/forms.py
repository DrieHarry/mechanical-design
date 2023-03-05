from django import forms
from .models import *


class MyForm(forms.Form):
    N = forms.FloatField(label="Faktor Keamanan ",
                            widget=forms.NumberInput(attrs={'value': '2.0', 'min': '0'}))
    RadioSelectTipe = forms.ChoiceField(label = "Pilih Tipe Poros" ,choices=(('1','Tipe 1'), ('2','Tipe 2')),
                                             initial='D', widget=forms.RadioSelect)
    RadioSelectDayaTorsi = forms.ChoiceField(label = "Pilih Input" ,choices=(('D','Daya'), ('T','Torsi')),
                                             initial='D', widget=forms.RadioSelect)
    P = forms.FloatField(label="Daya ",
                            widget=forms.NumberInput(attrs={'placeholder': 'kW'}),required=False)
    n = forms.FloatField(label="Kecepatan Putar ",
                            widget=forms.NumberInput(attrs={'placeholder': 'rpm'}),required=False)
    T = forms.FloatField(label="Torsi ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N-mm'}),required=False)
    Material = forms.ModelChoiceField(
                            label = "Pilih Bahan :", queryset = Materials.objects.all(),required=False)
    Ft = forms.FloatField(label="Gaya Tangensial Pada Elemen (Ft) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}),required=False)
    Fr = forms.FloatField(label="Gaya Radial Pada Elemen (Fr) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}),required=False)
    Ft1 = forms.FloatField(label="Gaya Tangensial Pada Elemen 1 (Ft1) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}),required=False)
    Fr1 = forms.FloatField(label="Gaya Radial Pada Elemen 1 (Fr1) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}),required=False)
    Ft2 = forms.FloatField(label="Gaya Tangensial Pada Elemen 2 (Ft2) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}),required=False)
    Fr2 = forms.FloatField(label="Gaya Radial Pada Elemen 2 (Fr2) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N', 'min': '0'}),required=False)
    AB = forms.FloatField(label="Jarak Antara Titik A ke Titik B (AB) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0'}),required=False)
    BC = forms.FloatField(label="Jarak Antara Titik C ke Titik B (BC) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0'}),required=False)
    CD = forms.FloatField(label="Jarak Antara Titik C ke Titik D (CD) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0'}),required=False)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        RadioSelectDayaTorsi = cleaned_data.get("RadioSelectDayaTorsi")
        P = cleaned_data.get("P")
        n = cleaned_data.get("n")
        T = cleaned_data.get("T")
        if RadioSelectDayaTorsi == 'D':
            if not P:
                raise forms.ValidationError('Daya harus diisi')
            if not n:
                raise forms.ValidationError('Kecepatan putar harus diisi')
        elif RadioSelectDayaTorsi == 'T':
            if not T:
                raise forms.ValidationError('Torsi harus diisi')
        return cleaned_data