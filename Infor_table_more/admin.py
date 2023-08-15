from django.contrib import admin
from .models import *
# Register your models here.
class Informacion_(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter= (["nombre"])
    search_fields = ['nombre']
    
admin.site.register(Informacion, Informacion_)
admin.site.register(Galeria)

admin.site.register(Tabla)
admin.site.register(Campos)