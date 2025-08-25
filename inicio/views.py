from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Club
from inicio.forms import FormularioClub

def inicio(request):
    return render(request, 'inicio.html')

def portal(request):

    print(request.POST)

    if request.method == 'POST':

        formulario = FormularioClub(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            club= Club(deportes=info.get('deportes'), categoria=info.get('categoria'))
            club.save()

            return redirect('lista_jugadores')
    
    else:
        formulario = FormularioClub()

    return render(request, 'club.html', {'formulario': formulario})

def lista_jugadores(request):

    jugadores = Club.objects.all()

    return render(request, 'lista_jugadores.html', {'jugadores': jugadores})
