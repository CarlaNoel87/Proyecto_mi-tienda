from django.shortcuts import render
# from django.http import HttpResponse
from inicio.models import Mantel
from inicio.forms import FormularioCrearMantel

def inicio(request):
      return render(request, "inicio.html")
    # return HttpResponse("<h1>¡Bienvenido a Mi Tienda!</h1>")
def armar_mantel(request):
    print(request.POST)
    if request.method == "POST":
        formulario = FormularioCrearMantel(request.POST)
        if formulario.is_valid():
          info= formulario.cleaned_data
          nuevo_mantel = Mantel(color=info.get("color"),material=info.get("material"), tamaño=info.get("tamaño"))
          nuevo_mantel.save()
          return render(request, "listado_de_mantel.html", {"mantel": nuevo_mantel})
    else:
        formulario = FormularioCrearMantel()
    return render(request, "mantel/armar.html",{"formulario": formulario})