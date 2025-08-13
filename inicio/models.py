from django.db import models


class Mantel(models.Model):
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)


    def __str__(self):
         return f"Mantel de {self.color}, {self.material}, {self.tamaño}"
