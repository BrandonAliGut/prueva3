from django.db import models


# Create your models here.

from django.utils.html import format_html

# Create your models here.
class Nivel_Informacion_base(models.Model):
    Categoria = models.CharField(max_length=50, blank=False, unique=True)
    Color = models.CharField(max_length=12, blank=False)
    Codigo_color = models.CharField(max_length=12, blank=False)
    Precio = models.CharField(max_length=3, blank=False, )
    Description = models.TextField()
    foto = models.ImageField(upload_to="Nivel_Informacion", blank= False, unique=False)
    
    def colored_first_name(self):

        
        return format_html(
        '<span style="color: {};">{}</span> <span style="color: {};">{}$</span>',self.Color,self.Categoria,self.Color,self.Precio
     
        )
    def __str__(self):
        return self.Categoria
    class Meta:
        verbose_name_plural = "Grado en categoria base"
