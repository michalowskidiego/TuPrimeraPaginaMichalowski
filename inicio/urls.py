from django.urls import path
from inicio.views import inicio, portal

urlpatterns = [
    path('inicio/', inicio),
    path('club/<deportes>/<edad>/', portal)
]