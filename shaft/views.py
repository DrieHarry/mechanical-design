from django.shortcuts import render


from .forms import *
from .models import *
from .perhitungan import tipe1, tipe2, get_recap


import math
import numpy as np
import matplotlib.pyplot as plt
 

# VIEWS FUNCTION
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
    
    # Pilihan tipe 1 atau tipe 2
    RadioTipe = request.POST['RadioSelectTipe']

    if RadioTipe == "1":
        results = tipe1(request)
        recaps = get_recap(request)

        return render(request, "shaft/output.html", {
            "results": results,
            "recaps": recaps,
        })

    if RadioTipe == "2":
        results = tipe2(request)
        recaps = get_recap(request)

        return render(request, "shaft/output.html", {
            "results": results,
            "recaps": recaps,
        })



def about(request):
    return render(request, "shaft/about.html")
