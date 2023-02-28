from django.shortcuts import render


from .forms import *
from .models import *


import math
import numpy as np
import matplotlib.pyplot as plt
 

# Create your views here.
def input(request):
    return render(request, "shaft/input.html", {
        "form": MyForm(),
    })

def output(request):
    form = MyForm(request.POST)
    if not form.is_valid():
        return render(request, "shaft/input.html", {
            "form": form,
        })
    
 #       cleaned_data = form.cleaned_data
 #       N = cleaned_data.get("N")
 #       RadioSelectDayaTorsi = cleaned_data.get("RadioSelectDayaTorsi")
 #       P = cleaned_data.get("P")
 #       n = cleaned_data.get("n")
 #       T = cleaned_data.get("T")
 #       Material = cleaned_data.get("Material")
 #       Ft = cleaned_data.get("Ft")
 #       Fr = cleaned_data.get("Fr")
 #       BC = cleaned_data.get("BC")
 #       Su = Material.tegangan_tarik
 #       Sy = Material.tegangan_luluh

    N = float(request.POST['N']) #Faktor Keamanan
    Ft = float(request.POST['Ft']) #Gaya Tangensial Pada Elemen
    Fr = float(request.POST['Fr']) #Gaya Radial Pada Elemen
    AB = float(request.POST['AB']) #Jarak Antara Bantalan A ke Elemen B
    BC = float(request.POST['BC']) #Jarak Antara Bantalan C ke Elemen B
    RadioDayaTorsi = request.POST['RadioSelectDayaTorsi'] # Pilihan memakai daya atau torsi
    
    #Bahan
    id = request.POST['Material']
    material = Materials.objects.get(id=id)
    Su = material.tegangan_tarik
    Sy = material.tegangan_luluh
    
    # Menghitung Torsi
    if RadioDayaTorsi == "D":
        P = float(request.POST['P']) #Daya
        n = float(request.POST['n']) #Kecepatan Putar
        T = (P * 1000 / (math.pi * n / 30) ) * 1000
    if RadioDayaTorsi == "T":
        Torsi = float(request.POST['T'])
        T = Torsi

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

    # Tegangan / Kekuatan Lelah Aktual Sn.Cs.Cr
    # Data Gambar 5.11 Kekuatan lelah vs Tegangan tarik
    data = np.array([(350, 138), (375, 143), (400, 150), (425, 163), (450, 172),
                 (475, 181), (500, 190), (525, 201), (550, 211), (575, 222),
                 (600, 227), (625, 237), (650, 247), (675, 254), (700, 263),
                 (725, 273), (750, 277), (775, 287), (800, 295), (825, 301),
                 (850, 311), (875, 319), (900, 325), (925, 335), (950, 343),
                 (975, 348), (1000, 352), (1025, 358), (1050, 365), (1075, 375),
                 (1100, 381), (1125, 388), (1150, 398), (1175, 402), (1200, 408), 
                 (1225, 413), (1250, 421), (1275, 425), (1300, 428), (1350, 437), 
                 (1400, 447), (1500, 457)])
    
    # Didapat x dan y
    x = data[:, 0]
    y = data[:, 1]
    # Memakai polynomial pangkat 15 ke data
    koefs = np.polyfit(x, y, 15)
    # Buat fungsi dari the koefisien
    poly_func = np.poly1d(koefs)
    # Plot gambar
    #plt.scatter(x, y)
    #plt.plot(x, poly_func(x), c='r')
    #plt.xlabel('x')
    #plt.ylabel('y')
    #plt.show()
    # Nilai Kekuatan Lelah
    S = poly_func(Su)
    # Kekuatan lelah aktual
    Sn = S * 0.75 * 0.81

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
        "Su": Su,
        "Sy": Sy,
        "T": T,
        "Sn": Sn
    })

def about(request):
    return render(request, "shaft/about.html")
