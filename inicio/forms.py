from django import forms

class FormularioClub(forms.Form):
    deportes = forms.CharField(max_length=20)
    categoria = forms.CharField(max_length=20)