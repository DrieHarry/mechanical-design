from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms


import math
 

class MyForm(forms.Form):
    N = forms.FloatField(label="Faktor Keamanan ",
                            widget=forms.NumberInput(attrs={'value': '2.0'}))
    T = forms.FloatField(label="Momen Puntir / Torsi ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N-mm'}))
    Sy = forms.FloatField(label="Tegangan Luluh Bahan ",
                            widget=forms.NumberInput(attrs={'placeholder': 'MPa'}))
    Sn = forms.FloatField(label="Tegangan / Kekuatan Lelah Aktual ",
                            widget=forms.NumberInput(attrs={'placeholder': 'MPa'}))
    Ft = forms.FloatField(label="Gaya Tangensial Pada Elemen (Ft) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N'}))
    Fr = forms.FloatField(label="Gaya Radial Pada Elemen (Fr) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'N'}))
    AB = forms.FloatField(label="Jarak Antara Bantalan A ke Elemen B (AB) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm'}))
    BC = forms.FloatField(label="Jarak Antara Bantalan C ke Elemen B (BC) ",
                            widget=forms.NumberInput(attrs={'placeholder': 'mm'}))


# Create your views here.
def input(request):
    return render(request, "shaft/input.html", {
        "form": MyForm()
    })

def output(request):

    N = float(request.POST['N']) #Faktor Keamanan
    T = float(request.POST['T']) #Torsi
    Sy = float(request.POST['Sy']) #Tegangan Luluh Bahan
    Sn = float(request.POST['Sn']) 
    Ft = float(request.POST['Ft']) #Gaya Tangensial Pada Elemen
    Fr = float(request.POST['Fr']) #Gaya Radial Pada Elemen
    AB = float(request.POST['AB']) #Jarak Antara Bantalan A ke Elemen B
    BC = float(request.POST['BC']) #Jarak Antara Bantalan C ke Elemen B

    # Menghitung Gaya Reaksi Tumpuan
    Az = (Ft * BC) / (AB + BC)
    Cz = (Ft * AB) / (AB + BC)
    Ay = (Fr * BC) / (AB + BC)
    Cy = (Fr * AB) / (AB + BC)

    # Menghitung Gaya Geser Gabungan
    Vc_horizontal = -Az + Ft
    Vc_vertikal = -Ay + Fr
    Vc_total = math.sqrt((Vc_horizontal)**2 + (Vc_vertikal)**2)

    # Menghitung Momen Lentur Gabungan
    M_horizontal = Az * AB
    M_vertikal = Ay * AB
    M_total = math.sqrt((M_horizontal)**2 + (M_vertikal)**2)

    # Kt lokasi bantalan 2.0; roda gigi 2.5
    # Momen Lentur pada titik A = 0
    result_a = ((32 * N) / math.pi * math.sqrt(((2.5 * 0) / Sn)**2 + (3/4 * (T / Sy)**2)))**(1/3)
    result_b = ((32 * N) / math.pi * math.sqrt(((2.0 * M_total) / Sn)**2 + (3/4 * (T / Sy)**2)))**(1/3)
    # Tidak ada momen lentur dan torsi pada titik C maka,
    result_c = math.sqrt((2.94 * 2.5 * Vc_total * N) / Sn)

    return render(request, "shaft/output.html", {
        "result_a": result_a,
        "result_b": result_b,
        "result_c": result_c,
    })

def about(request):
    return render(request, "shaft/about.html")
