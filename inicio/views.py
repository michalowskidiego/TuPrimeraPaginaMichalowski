from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Club

def inicio(request):
    return render(request, 'inicio.html')

def portal(request, deportes, edad):

    club= Club(deportes=deportes, edad=edad)
    club.save()

    return render(request, 'club.html', {'club': club})
