from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from twilio.rest import Client

from .forms import TelefonoForm

from consultas.models import Validacion

import random

account_sid=settings.ACCOUNT_SID
auth_token=settings.AUTH_TOKEN


def home(request):
    return render(request, 'home.html', {})

def inicio_test(request):
    return render(request, 'autoevaluacion.html', {})

def pagina_dos(request):
    return render(request, 'autoevaluacion2.html', {})

def telefono(request):
    context = {}
    form = TelefonoForm
    context['form'] = form
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            codigo = random.randint(100000,999999)
            validacion_qs = Validacion.objects.filter(
                telefono=telefono,
                estado='Activo')
            if validacion_qs:
                for elemento in validacion_qs:
                    estado = 'Cancelado'
                    elemento.estado = estado
                    elemento.save()
            validacion = Validacion.objects.create(
                telefono=telefono,
                codigo=codigo,
                estado='Activo'
            )
            client = Client(account_sid, auth_token)
            body = 'Coronabogota. Tu código es {codigo}'.format(codigo=codigo)
            to = '+57{telefono}'.format(telefono=telefono)
            message = client.messages.create(
                to=to,
                from_="+12567810930",
                body=body)
            request.session['telefono'] = telefono
            return HttpResponseRedirect(reverse('validacion_telefono'))
    return render(request, 'telefono.html', context)

def validacion_telefono(request):
    telefono = request.session['telefono']
    validacion = Validacion.objects.filter(telefono=telefono, estado='Activo').first()
    print('telefono')
    if request.method == 'POST':
        codigo = validacion.codigo
        valor1 = str(request.POST['valor1'])
        valor2 = str(request.POST['valor2'])
        valor3 = str(request.POST['valor3'])
        valor4 = str(request.POST['valor4'])
        valor5 = str(request.POST['valor5'])
        valor6 = str(request.POST['valor6'])
        codigo_metido = '{valor1}{valor2}{valor3}{valor4}{valor5}{valor6}'.format(
            valor1=valor1,
            valor2=valor2,
            valor3=valor3,
            valor4=valor4,
            valor5=valor5,
            valor6=valor6
        )
        if str(codigo_metido) == str(codigo):
            estado = 'Usado'
            validacion.estado = estado
            return HttpResponseRedirect(reverse('geolocalizacion'))
            print('adelante')
    return render(request, 'confirmacion_telefono.html', {})

def geolocalizacion(request):
    if request.method == 'POST':
        request.session['lat'] = request.POST.get('lat')
        request.session['long'] = request.POST.get('long')
        return HttpResponseRedirect(reverse('consultas:datos_personales'))
        # print(request.POST)
    return render(request, 'geolocalizacion.html', {})
