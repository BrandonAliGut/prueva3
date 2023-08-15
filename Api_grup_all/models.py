from django.db import models
from django.utils.safestring import mark_safe
from Pagos_zooapp_items.models import *

# Create your models here.

class GrupoAnimals(models.Model):
    def fotoGrupo(self):
        return mark_safe('<a href = "/media/%s"><img src="/media/%s" height = 200px width =260  /> </a>'%(self.foto, self.foto))
    idGrup = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length= 100, blank = True, unique= False)
    foto = models.ImageField(upload_to ="Grupo" , blank= False, unique=False)
    activo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.grupo
    class Meta:
        verbose_name_plural= "Grupos"

class ListAnimalGrupos(models.Model):
    def fotoAnim(self):
        return mark_safe('<div style="display:flex; justify-content: center; align-items: center; "> <a href = "/media/{}"><img src="/media/{}" height = 200px   /> </a></div>'.format(self.foto, self.foto,GrupoAnimals.grupo))
    idAnimalList = models.AutoField(primary_key=True)
    AnimalList= models.CharField(max_length= 100, blank=False, unique= False)
    foto= models.ImageField(upload_to ="Lista_De_Animales", blank= False, unique=False)
    PGRUPO=models.ForeignKey(GrupoAnimals, on_delete= models.CASCADE, blank= True)
    
    activo = models.BooleanField(default=False)
    
    #Aqui
    def __str__(self):
        return (self.AnimalList)
    class Meta:
        verbose_name_plural= "Lista de Especie"
        ordering = ['PGRUPO']

class MenuButton(models.Model):
    def fotoMenu(self):
        if self.opcion == "A": 
            return mark_safe(
                '<div style="display:flex; justify-content: center; align-items: center; "> <a href = "/media/%s"><img src="/media/%s" height = 200px   /> <h2 style="text-align: center; background-color: rgba(255, 255, 255, 0); color: black;">Menu</h2> </a></div>'%(self.foto, self.foto)
                )
        elif self.opcion == "B":
            return mark_safe(
                '<div style="display:flex; justify-content: center; align-items: center; "> <a href = "/media/%s"><img src="/media/%s" height = 200px   /> <h2 style="text-align: center; background-color: rgba(255, 255, 255, 0); color: black;">Directo</h2> </a></div>'%(self.foto, self.foto)
                )
            
    Opc_tipo = ( ('A', 'Menu'),
                ('B', 'Directo'),
                )
    id_MenuButton= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=40, blank= False, unique= True)
    opcion= models.CharField(max_length=1, choices= Opc_tipo )
    foto = models.ImageField(upload_to="MenuButton", blank= False, unique=False)
    PGRUPO=models.ForeignKey(ListAnimalGrupos, on_delete= models.CASCADE, blank= True)
    activo = models.BooleanField(default=False)
    def colored_name(self):
        if self.opcion == "A": 
            return format_html(
                '<span style="color: 1,0,0,1;">{} {}</span>'.format(self.titulo, self.opcion)
            )
            
    def __str__(self):
        opc= str()
        if self.opcion =="A":
            opc= "Menu"
        else:
            opc= "Directo"
        
        return self.titulo
    class Meta:
        verbose_name_plural= "Menu Principal"
        
class Lista(models.Model):
    def type_menu_opc(self):
        opc= str()
        if self.PGRUPO.opcion =="A":
            opc= "Menu"
            if self.PGRUPO.opcion == "A":
                return mark_safe(
                    '<div style="display:flex; justify-content: center; align-items: center; "> <a href = "/media/%s"><img src="/media/%s" height = 200px   /> <h2 style="text-align: center; background-color: rgba(255, 255, 255, 0); color: black;">Menu</h2> </a></div>'%(self.PGRUPO.foto, self.PGRUPO.foto)
                )
            elif self.PGRUPO.opcion == "B":
                return mark_safe(
                    '<div style="display:flex; justify-content: center; align-items: center; "> <a href = "/media/%s"><img src="/media/%s" height = 200px   /> <h2 style="text-align: center; background-color: rgba(255, 255, 255, 0); color: black;">Directo</h2> </a></div>'%(self.PGRUPO.foto, self.PGRUPO.foto)
            )
        else:
            opc= "Error No Compatible"
            return mark_safe('<p style="color: red;">%s (%s)</p>' %(self.nombre,opc))
        
    nombre = models.CharField(max_length= 255, blank= False)
    PGRUPO=models.ForeignKey(MenuButton, on_delete= models.CASCADE, blank= True)
    activo = models.BooleanField(default=False)
    def __str__(self):
        opc= str()
        if self.PGRUPO.opcion =="A":
            opc= "Menu"
        else:
            opc= "Error"
        
        return "{}  ->({})".format(self.nombre,opc)
    class Meta:
        verbose_name_plural= "Menu lista"
        




