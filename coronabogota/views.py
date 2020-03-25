from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def inicio_test(request):
    return render(request, 'autoevaluacion.html', {})
