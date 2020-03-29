from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .forms import PersonaForm
from .models import Consulta, Ciudad, Persona
# Create your views here.

class ConsultaListView(ListView):
    model = Consulta

    def get_context_data(self, *args, **kwargs):
        context = super(ConsultaListView, self).get_context_data(*args, **kwargs)
        ciudades = Ciudad.objects.all()
        context['ciudades'] = ciudades
        return context

    def get_queryset(self, *args, **kwargs):
        ciudades_qs = Ciudad.objects.all()
        ciudades_list = []
        for ciudad in ciudades_qs:
            ciudades_list.append(ciudad.nombre)
        gravedad_list = ['Baja', 'Media', 'Alta']
        ciudades = []
        gravedad = []
        for key, value in self.request.GET.items():
            if key in ciudades_list:
                ciudades.append(value)
            if key in gravedad_list:
                gravedad.append(value)
        qs = super(ConsultaListView, self).get_queryset(*args, **kwargs)
        if ciudades:
            qs = qs.filter(ciudad__in=ciudades)
        if gravedad:
            qs = qs.filter(gravedad__in=gravedad)
        return qs

class PersonaView(CreateView):
    model = Persona
    form_class = PersonaForm

    def form_valid(self, form, *args, **kwargs):
        result = super(PersonaView, self).form_valid(form, *args, **kwargs)
        print(self.request.session['telefono'], self.request.session['lat'], self.request.session['long'])
        consulta = Consulta.objects.create(
            telefono=self.request.session['telefono'],
            lat=self.request.session['lat'],
            long=self.request.session['long'],
            ciudadano=self.object
            )
        return result

    def get_success_url(self):
        return reverse('preguntas:pregunta', kwargs={'pk': 1})
