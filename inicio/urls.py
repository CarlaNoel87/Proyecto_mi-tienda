from django.urls import path
from inicio.views import inicio, armar_mantel   

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("mantel/armar/", armar_mantel, name="armar_mantel"),
    # path("mantel/armar/<str:color>/<str:material>/<str:tamaño>/", armar_mantel, name="armar_mantel"),
]
