from django.urls import path
from .views import (
    PreguntaDetailView
        )

urlpatterns = [
    path('<pk>/', PreguntaDetailView.as_view(), name='pregunta'),
]
