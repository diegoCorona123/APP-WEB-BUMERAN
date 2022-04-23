
from django.db import models
import datetime 

class empleo(models.Model):
    
    titulo = models.CharField(max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField(default=datetime.date.today, blank=False, null=False)
    disponible= models.BooleanField(default=True)
    descripcion= models.TextField( blank=False, null= False)
    fecha= models.DateField( blank=False, null= False)
    empleo= models.CharField( max_length=100, blank=False, null=False)
    empleos_disponibles = models.IntegerField(null=True)
    enlace =models.URLField()
    imagen= models.ImageField( null=True, upload_to='empleo')
    empresa= models.CharField( max_length=100, blank=False, null=False) 
    sueldo=models.IntegerField( null=False)
    ciudad = models.CharField( max_length=100,blank=False, null= False)
    email=models.EmailField()


    def __str__(self):
        return self.empleo

class Comentarios(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    motivo = models.CharField(max_length=100, blank=False, null=False)
    comentario = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.nombre
        
   
# Create your models here.


