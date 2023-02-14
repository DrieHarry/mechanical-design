from django.shortcuts import render


# Create your views here.
def input(request):
    return render(request, "shaft/input.html")

def output(request):
    return render(request, "shaft/output.html")

def about(request):
    return render(request, "shaft/about.html")
