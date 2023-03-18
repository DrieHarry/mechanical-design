from django import forms
from .models import *


class MyForm(forms.Form):
    N = forms.FloatField(label="Faktor Keamanan ",
                            widget=forms.NumberInput(attrs={'value': '2.0', 'min': '0', 'class':'form-control'}))
    RadioSelectTipe = forms.ChoiceField(label = "Pilih Tipe Poros" ,choices=(('1','Tipe 1'), ('2','Tipe 2')),
                                            initial = "",widget=forms.RadioSelect,required=False)
    RadioSelectDayaTorsi = forms.ChoiceField(label = "Pilih Input" ,choices=(('D','Daya'), ('T','Torsi')),
                                            initial = "", widget=forms.RadioSelect,required=False)
    P = forms.FloatField(label="Daya ",
                            widget=forms.NumberInput(attrs={'placeholder': 'kW', 'class':'form-control'}),required=False)
    n = forms.FloatField(label="Kecepatan Putar ",
                            widget=forms.NumberInput(attrs={'placeholder': 'rpm', 'class':'form-control'}),required=False)
    T = forms.FloatField(label="Torsi ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N-mm', 'class':'form-control'}),required=False)
    Material = forms.ModelChoiceField(
                            label = "Pilih Bahan :", queryset = Materials.objects.all(),required=False,widget=forms.Select(attrs={'class': 'form-select'}))
    Ft = forms.FloatField(label="Gaya Tangensial Pada Elemen (Ft) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'Newton', 'min': '0', 'class':'form-control'}),required=False)
    Fr = forms.FloatField(label="Gaya Radial Pada Elemen (Fr) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'Newton', 'min': '0', 'class':'form-control'}),required=False)
    Ft1 = forms.FloatField(label="Gaya Tangensial Pada Elemen 1 (Ft1) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'Newton', 'min': '0', 'class':'form-control'}),required=False)
    Fr1 = forms.FloatField(label="Gaya Radial Pada Elemen 1 (Fr1) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'Newton', 'min': '0', 'class':'form-control'}),required=False)
    Ft2 = forms.FloatField(label="Gaya Tangensial Pada Elemen 2 (Ft2) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'Newton', 'min': '0', 'class':'form-control'}),required=False)
    Fr2 = forms.FloatField(label="Gaya Radial Pada Elemen 2 (Fr2) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'Newton', 'min': '0', 'class':'form-control'}),required=False)
    AB = forms.FloatField(label="Jarak Antara Titik A ke Titik B (AB) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0', 'class':'form-control'}),required=False)
    BC = forms.FloatField(label="Jarak Antara Titik C ke Titik B (BC) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0', 'class':'form-control'}),required=False)
    CD = forms.FloatField(label="Jarak Antara Titik C ke Titik D (CD) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm', 'min': '0', 'class':'form-control'}),required=False)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        tipe = cleaned_data.get("RadioSelectTipe")
        RadioSelectDayaTorsi = cleaned_data.get("RadioSelectDayaTorsi")
        P = cleaned_data.get("P")
        n = cleaned_data.get("n")
        T = cleaned_data.get("T")
        AB = cleaned_data.get("AB")
        BC = cleaned_data.get("BC")
        errors = []
        if not tipe:
            errors.append('Pilih Tipe!')
        if not RadioSelectDayaTorsi:
            errors.append('Pilih Input Daya/Torsi!')
        if RadioSelectDayaTorsi == 'D':
            if not P:
                errors.append('Daya harus diisi!')
            if not n:
                errors.append('Kecepatan putar harus diisi!')
        elif RadioSelectDayaTorsi == 'T':
            if not T:
                errors.append('Torsi harus diisi!')
        if tipe == '1':
            Ft = cleaned_data.get("Ft")
            Fr = cleaned_data.get("Fr")
            if not Ft:
                errors.append('Gaya Tangensial harus diisi!')
            if not Fr:
                errors.append('Gaya Radial harus diisi!')
            if not AB:
                errors.append('Jarak Antara Titik A ke Titik B (AB) harus diisi!')
            if not BC:
                errors.append('Jarak Antara Titik B ke Titik C (BC) harus diisi!')
        if tipe == '2':
            Ft1 = cleaned_data.get("Ft1")
            Fr1 = cleaned_data.get("Fr1")
            Ft2 = cleaned_data.get("Ft2")
            Fr2 = cleaned_data.get("Fr2")
            CD = cleaned_data.get("CD")
            if not Ft1:
                errors.append('Gaya Tangensial harus diisi!')
            if not Fr1:
                errors.append('Gaya Radial harus diisi!')
            if not Ft2:
                errors.append('Gaya Tangensial harus diisi!')
            if not Fr2:
                errors.append('Gaya Radial harus diisi!')
            if not AB:
                errors.append('Jarak Antara Titik A ke Titik B (AB) harus diisi!')
            if not BC:
                errors.append('Jarak Antara Titik B ke Titik C (BC) harus diisi!')
            if not CD:
                errors.append('Jarak Antara Titik C ke Titik D (CD) harus diisi!')
        if errors:
            raise forms.ValidationError(errors)