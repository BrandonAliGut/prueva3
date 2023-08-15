from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)

class User_Perfil_add(admin.ModelAdmin):
    list_display = ("user","Nombre","Activo_store", "Fecha_registro")
    list_filter= (["user"])
    search_fields=  ("ID_DECOMPRA", "Nombre", "Fecha_registro","user")
    
admin.site.register(User_Perfil,User_Perfil_add)