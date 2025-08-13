from django import forms
class FormularioCrearMantel(forms.Form):
    color = forms.CharField(max_length=50)
    material = forms.CharField(max_length=50)
    tamaño = forms.CharField(max_length=50)

    