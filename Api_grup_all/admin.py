from django.contrib import admin
from .models import *
# Register your models here.
class GrupoAdmin(admin.ModelAdmin):
    list_display = ['grupo','fotoGrupo',]
    search_fields= ['grupo']


class ListAnimalGrupoAdmin(admin.ModelAdmin):
    list_display = ['PGRUPO','AnimalList','fotoAnim']
    list_filter= (["AnimalList"])
    search_fields = ['AnimalList']
    
class MenuButton_return(admin.ModelAdmin):
    list_display = ['titulo', 'opcion', 'fotoMenu']
    list_filter= (["titulo"])
    search_fields = ['titulo','opcion']

class Lista_admin(admin.ModelAdmin):
    list_display = ['nombre', 'type_menu_opc']
    list_filter= (["nombre"])
    search_fields = ['nombre']




    
admin.site.register(GrupoAnimals, GrupoAdmin)
admin.site.register(ListAnimalGrupos, ListAnimalGrupoAdmin)
admin.site.register(MenuButton, MenuButton_return)
admin.site.register(Lista, Lista_admin)




