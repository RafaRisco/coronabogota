from django.urls import path
from .views import (
    PreguntaDetailView,
    ResultadoView
        )

urlpatterns = [
    path('resultado/', ResultadoView.as_view(), name='resultado'),
    path('<pk>/', PreguntaDetailView.as_view(), name='pregunta'),
]
