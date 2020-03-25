from django.urls import path
from .views import (
        ConsultaListView,
        )

urlpatterns = [
    path('lista/', ConsultaListView.as_view(), name='lista'),
]
