from django.urls import path
from .views import (
        ConsultaListView,
        PersonaView
        )

urlpatterns = [
    path('lista/', ConsultaListView.as_view(), name='lista'),
    path('datos_personales/', PersonaView.as_view(), name='datos_personales'),
]
