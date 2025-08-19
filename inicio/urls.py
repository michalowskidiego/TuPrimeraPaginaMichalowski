from django.urls import path
from inicio.views import inicio, portal, lista_jugadores

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('club/', portal, name='portal'),
    path('lista-jugadores/', lista_jugadores, name='lista_jugadores'),
]