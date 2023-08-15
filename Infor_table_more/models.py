from django.db import models

from Api_grup_all.models import *
# Create your models here.


class Informacion(models.Model):
    Tipo= [
        ("MenuButton","MenuButton"),
        ("Lista","Lista")
    ]
    nombre = models.CharField(max_length=40, blank= False)
    texto =models.TextField()
    
    PGRUPO=models.ForeignKey(MenuButton, on_delete= models.CASCADE, blank= True, null=True)
    PGRUPO_Lista = models.ForeignKey(Lista,on_delete= models.CASCADE, blank = True, null=True)
    padre = models.CharField(max_length=40, blank= False,choices=Tipo, default="MenuButton")
    activo = models.BooleanField(default=False) 
    def __str__(self):
        
        return self.nombre     
    class Meta:
        verbose_name_plural= "Informacion"
        
class Galeria(models.Model):
    nombre = models.CharField(max_length=40, blank= True, null= True)
    foto = models.ImageField(upload_to= "Galeria_Inform", blank= True, )
    id_Info = models.ForeignKey(Informacion, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.nombre



class Tabla(models.Model):
    name= models.CharField(max_length=255,blank=False, null=False)
    id_Info = models.ForeignKey(Informacion,on_delete= models.CASCADE, blank = True, null=True)
    def __str__(self):
        return self.name

class Campos(models.Model):
    name= models.CharField(max_length=255,blank=False, null=False)
    descripcion=models.TextField(blank=False, null=False)
    id_tabla = models.ForeignKey(Tabla, on_delete=models.CASCADE, blank=True, null=True)
    
class Tabla_campo(models.QuerySet):
    pass