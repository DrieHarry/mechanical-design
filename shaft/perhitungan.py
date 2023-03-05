from .models import *


import math
import numpy as np
import matplotlib.pyplot as plt

def get_post(request):
    N = float(request.POST['N']) #Faktor Keamanan
    AB = float(request.POST['AB']) #Jarak Antara Bantalan A ke Elemen B
    BC = float(request.POST['BC']) #Jarak Antara Bantalan C ke Elemen B
    RadioDayaTorsi = request.POST['RadioSelectDayaTorsi'] # Pilihan memakai daya atau torsi

    # Bahan
    id = request.POST['Material']
    material = Materials.objects.get(id=id)
    Su = material.tegangan_tarik
    Sy = material.tegangan_luluh
    
    RadioTipe = request.POST['RadioSelectTipe']
    if RadioTipe == "1":
        Ft = float(request.POST['Ft']) #Gaya Tangensial Pada Elemen
        Fr = float(request.POST['Fr']) #Gaya Radial Pada Elemen
        return N, Ft, Fr, AB, BC, RadioDayaTorsi, Su, Sy
    
    if RadioTipe == "2":
        Ft1 = float(request.POST['Ft1']) #Gaya Tangensial Pada Elemen
        Fr1 = float(request.POST['Fr1']) #Gaya Radial Pada Elemen
        Ft2 = float(request.POST['Ft2']) #Gaya Tangensial Pada Elemen
        Fr2 = float(request.POST['Fr2']) #Gaya Radial Pada Elemen
        CD = float(request.POST['CD']) #Jarak Antara Bantalan C ke Elemen B
        return N, Ft1, Fr1, Ft2, Fr2, AB, BC, CD, RadioDayaTorsi, Su, Sy


def kekuatan_lelah_aktual(Su):
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
    # Tegangan / Kekuatan Lelah Aktual Sn.Cs.Cr
    Sn = S * 0.75 * 0.81
    return Sn

def tipe1(request):
    # Akses Input
    N, Ft, Fr, AB, BC, RadioDayaTorsi, Su, Sy = get_post(request)

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

    # Kekuatan Lelah Aktual
    Sn = kekuatan_lelah_aktual(Su)

    # Kt lokasi bantalan 2.5; roda gigi 2.0
    # Momen Lentur pada titik A = 0
    result_a = ((32 * N) / math.pi * math.sqrt(((2.5 * 0) / Sn)**2 + (3/4 * (T / Sy)**2)))**(1/3)
    result_b = ((32 * N) / math.pi * math.sqrt(((2.0 * M_total) / Sn)**2 + (3/4 * (T / Sy)**2)))**(1/3)
    # Tidak ada momen lentur dan torsi pada titik C maka,
    result_c = math.sqrt((2.94 * 2.5 * Vc_total * N) / Sn)

    return result_a, result_b, result_c

def tipe2(request):
    N, Ft1, Fr1, Ft2, Fr2, AB, BC, CD, RadioDayaTorsi, Su, Sy = get_post(request)
    
    # Menghitung Torsi
    if RadioDayaTorsi == "D":
        P = float(request.POST['P']) #Daya
        n = float(request.POST['n']) #Kecepatan Putar
        T = (P * 1000 / (math.pi * n / 30) ) * 1000
    if RadioDayaTorsi == "T":
        Torsi = float(request.POST['T'])
        T = Torsi

    # Menghitung Gaya Reaksi Tumpuan
    Az = ((Ft1 * (BC+CD)) - (Ft2*CD)) / (AB + BC + CD)
    Dz = ((Ft2 * (BC+AB)) - (Ft1*AB)) / (AB + BC + CD)
    Ay = ((Fr1 * (BC+CD)) + (Fr2*CD)) / (AB + BC + CD)
    Dy = ((Fr2 * (BC+AB)) + (Fr1*AB)) / (AB + BC + CD)

    # Menghitung Gaya Geser Gabungan
    Vab_horizontal = Az
    Vbc_vertikal = Ay
    Vcd_horizontal = Az - Ft1 + Ft2
    Vcd_vertikal = Ay - Fr1 - Fr2
    Vab_total = math.sqrt((Vab_horizontal)**2 + (Vbc_vertikal)**2)
    Vcd_total = math.sqrt((Vcd_horizontal)**2 + (Vcd_vertikal)**2)
    print(Vcd_horizontal, Vcd_vertikal)

    # Menghitung Momen Lentur Gabungan
    Mb_horizontal = Az * AB
    Mb_vertikal = Ay * AB
    Mc_horizontal = (Az * (AB+BC)) - (Ft1*BC)
    Mc_vertikal = (Ay * (AB+BC)) - (Fr1*BC)
    Mb_total = math.sqrt((Mb_horizontal)**2 + (Mb_vertikal)**2)
    Mc_total = math.sqrt((Mc_horizontal)**2 + (Mc_vertikal)**2)

    # Kekuatan Lelah Aktual
    Sn = kekuatan_lelah_aktual(Su)
    print(f"Sn = {Sn}")
    print(f"Vab = {Vab_total}")
    print(f"Vcd = {Vcd_total}")
    print(f"Mb = {Mb_total}")
    print(f"Mc = {Mc_total}")

    # Kt lokasi bantalan 2.0; roda gigi 2.5
    # Titik A Gaya Geser
    result_a = math.sqrt((2.94 * 2.0 * Vab_total * N) / Sn)
    # Titik B Torsi dan Momen
    result_b= ((32 * N) / math.pi * math.sqrt(((2.5 * Mb_total) / Sn)**2 + (3/4 * (T / Sy)**2)))**(1/3)
    # Titik C Torsi dan Momen
    result_c= ((32 * N) / math.pi * math.sqrt(((2.5 * Mc_total) / Sn)**2 + (3/4 * (T / Sy)**2)))**(1/3)
    # Titik D Gaya Geser,
    result_d = math.sqrt((2.94 * 2.0 * Vcd_total * N) / Sn)

    return result_a, result_b, result_c, result_d