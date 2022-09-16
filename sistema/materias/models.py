from django.db import models

# Create your models here.
class Cursor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Estudiante')
    profesor = models.CharField(max_length=50, verbose_name='Profesor')
    materia = models.CharField(max_length=50, verbose_name='Materia')
    
    def __str__(self):
        fila = "Estudiante: " + self.nombre + " - " + "Materia: " + self.materia
        return fila
    
    