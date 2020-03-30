from django.urls import reverse
from django.shortcuts import render
from django.views.generic import DetailView, FormView, TemplateView
from django.views.generic.edit import CreateView

# Create your views here.
from consultas.models import Consulta

from .forms import RespuestaForm
from .models import Pregunta, Respuesta


class PreguntaDetailView(FormView, DetailView):
    model = Pregunta
    form_class = RespuestaForm

    def get_context_data(self, *args, **kwargs):
        context = super(PreguntaDetailView, self).get_context_data(*args, **kwargs)
        context['form'] = RespuestaForm()
        return context

    def form_valid(self, form, *args, **kwargs):
        telefono = self.request.session['telefono']
        respuesta_a_pregunta = form.cleaned_data['titulo']
        pregunta = self.get_object()
        consulta = Consulta.objects.filter(
            telefono=telefono
        ).last()
        self.request.session['consulta'] = consulta.pk
        respuesta = Respuesta.objects.create(
            consulta=consulta,
            pregunta=pregunta,
            titulo=respuesta_a_pregunta
        )
        return super(PreguntaDetailView, self).form_valid(form, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        pregunta = self.get_object()
        pk = pregunta.pk
        nuevo_pk = pk + 1
        preguntas = len(Pregunta.objects.all())
        if nuevo_pk > preguntas:
            return reverse('preguntas:resultado')
        return reverse('preguntas:pregunta', kwargs={'pk': nuevo_pk})

class ResultadoView(TemplateView):
    template_name='resultados.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultadoView, self).get_context_data(*args, **kwargs)
        print(self.request.session['consulta'])
        consulta = Consulta.objects.filter(pk=self.request.session['consulta']).first()
        context['consulta'] = consulta
        return context
