from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'inicio.html')

def analisis(request):
    return render(request, 'AnalisisDatos.html')