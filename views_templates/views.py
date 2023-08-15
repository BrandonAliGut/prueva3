from django.shortcuts import render, redirect
from Api_grup_all.models import *
from Api_grup_all.form import *

from Infor_table_more.models import *
from Infor_table_more.form import *
from django.views import View

from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q

from django.contrib.auth.decorators import permission_required
# Create your views here.
#'Api_grup_all.change_grupoanimals', 12b12b12b
#'Api_grup_all.delete_grupoanimals'
"""
class View_admin_base(View):
    def get(self, request):
        return request()"""

@permission_required('Api_grup_all.change_grupoanimals')
def group_admin(request, pk=1): 
    try:
        page_number = request.GET.get('page')
        grupo = GrupoAnimals.objects.all()
        paginator= Paginator(grupo, 6)
        page_obj = paginator.get_page(page_number)
        
        
        
        
      
        try:
            grupo_pk = GrupoAnimals.objects.get(idGrup=pk)
            lista_pk = ListAnimalGrupos.objects.filter(PGRUPO=pk)
        except GrupoAnimals.DoesNotExist:
            grupo_pk=GrupoAnimals.objects.latest('idGrup')
            

        if request.user.is_authenticated:
            user_name= request.user
            if request.method == "POST":
                
                class_form = GrupForm(request.POST,request.FILES, instance=grupo_pk)
                if class_form.is_valid():
                    class_form.save()
                    messages.success(request, f'update success')
            else:
                class_form= GrupForm(instance=grupo_pk)
            data= {
                "user":user_name,
                "grupos": page_obj,
                "grupo_pk":grupo_pk,
                "form": class_form,
                "lista_pk":lista_pk
                
                
            }
        else:
            if not request.user.is_authenticated:
                return redirect('login')
            return redirect('all_grup')

        return render(request, "viewgroup/home_admin.html", data)
    except: 
        return redirect("all_grup")

@permission_required('Api_grup_all.add_grupoanimals')
def grup_add(request):
    if request.method =="POST":
       
        class_form = GrupForm(request.POST,request.FILES)
       
        if class_form.is_valid():
            __save =class_form.save()
            grupo_name = class_form.cleaned_data.get('grupo')
            Grupo=__save
            messages.success(request, f"add success ' {grupo_name} '")
            return redirect(f'select_grup',Grupo.idGrup)
    else:
        class_form = GrupForm()
    data = {
        "form": class_form
    }

    
    return render(request, "form/grup_add.html", data)

@permission_required('Api_grup_all.delete_grupoanimals')
def grup_delete(request, pk):
    try:
        class_grupo = GrupoAnimals.objects.get(pk=pk)
    except GrupoAnimals.DoesNotExist:
        messages.success(request, f'error delete')
        return redirect('select_grup', pk)
    class_grupo.delete()
    messages.success(request, f"se a eliminado corectamente ' {class_grupo} '")
    return redirect('home_grupo')
    
class Page_grup(PermissionRequiredMixin,ListView):
    permission_required= (
        'Api_grup_all.view_grupoanimals'
    )
    template_name= "viewgroup/pagiall.html"
    model = GrupoAnimals
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try: 
                """content_type = ContentType.objects.get_for_model(GrupoAnimals)
                permission_group = Permission.objects.filter(content_type =content_type)
                print( [perm.codename for perm in permission_group])"""
                grupo = GrupoAnimals.objects.all()
                page_number = request.GET.get('page')
                paginator= Paginator(grupo, 12)
                
                page_obj = paginator.get_page(page_number)
                data= {
                "grupos": grupo,
                "pages":page_obj,
                }
                return render(request, "viewgroup/pagiall.html", data)
            except GrupoAnimals.DoesNotExist:
                messages.success(request,'Error: la ruta no existe ')
                return redirect('home')
        return redirect('home')

# Especies funciones vasadas en vista y classes 
@permission_required('Api_grup_all.change_grupoanimals')
def group_Especies(request, pk=1): 
  
    page_number = request.GET.get('page')
    grupoanimals = GrupoAnimals.objects.all()
    grupo = ListAnimalGrupos.objects.order_by("PGRUPO")
    paginator= Paginator(grupo, 6)
    page_obj = paginator.get_page(page_number)
    
    try:
        grupo_pk = ListAnimalGrupos.objects.get(idAnimalList=pk)
        lista_pk = GrupoAnimals.objects.filter(grupo=grupo_pk.PGRUPO) 
        menu_button = MenuButton.objects.filter(PGRUPO = pk)
         
    except ListAnimalGrupos.DoesNotExist:
        grupo_pk=ListAnimalGrupos.objects.latest('idAnimalList')
        
    data2=[{
        "lista_pk": lista_pk,
        "menu_button":menu_button
    }]

    if request.user.is_authenticated:
        user_name= request.user
        if request.method == "POST":
           
            class_form = GrupEspecies(request.POST,request.FILES, instance=grupo_pk)
            if class_form.is_valid():
                class_form.save()
                messages.success(request, f'update success')
        else:
            class_form= GrupEspecies(instance=grupo_pk)
        data= {
            "user":user_name,
            "grupos": page_obj,
            "grupo_pk":grupo_pk,
            "form": class_form,
            "datas_extra": data2,
            "grupoAnimalas": grupoanimals
            
            
        }
    else:
        if not request.user.is_authenticated:
            return redirect('login')
        return redirect('all_grup')

    return render(request, "view_species/update_especies.html", data)

def Especie_add(request):

    if request.method =="POST":
        
        class_form = GrupEspecies(request.POST,request.FILES)
        
        if class_form.is_valid():
            try: 
                
                __save = class_form.save()
                
                
                grupo_name = class_form.cleaned_data.get('AnimalList')
                Grupo=__save
                
                messages.success(request, f"add success ' {grupo_name} '")
                return redirect(f'select_species',Grupo.idAnimalList)
            except:
                messages.success(request, 'Error En Los Datos Ingresado')
                return redirect('home_animals_grupo')
    else:
        class_form = GrupEspecies()
    data = {
        "form": class_form
    }
    return render(request, "view_species/form/form_add.html", data)
def Especie_delete(request, pk):
    try:
        class_grupo = ListAnimalGrupos.objects.get(pk=pk)
    except ListAnimalGrupos.DoesNotExist:
        messages.success(request, f'error delete')
        return redirect('select_species', pk)
    class_grupo.delete()
    messages.success(request, f"se a eliminado corectamente ' {class_grupo} '")
    return redirect('home_animals_grupo')

#funcion para la vista menu

def group_Menu(request, pk=1): 
  
    page_number = request.GET.get('page')
    
    grupo = MenuButton.objects.all()
    paginator= Paginator(grupo, 6)
    page_obj = paginator.get_page(page_number)
    list = None
    try:
        grupo_pk = MenuButton.objects.get(id_MenuButton=pk)
        lista_pk = ListAnimalGrupos.objects.filter(idAnimalList=grupo_pk.PGRUPO.idAnimalList) 
        lista_group = GrupoAnimals.objects.filter(grupo=grupo_pk.PGRUPO.PGRUPO)
        
        if lista_pk == None:
            list = None
        else:
            list = lista_pk
        
    except MenuButton.DoesNotExist:
        grupo_pk=MenuButton.objects.latest('id_MenuButton')
    data2=[{
        "lista_pk": list,
        "lista_group":lista_group
    }]
    
    if request.user.is_authenticated:
        user_name= request.user
        if request.method == "POST":
            
            class_form = MenuButtonForm(request.POST,request.FILES, instance=grupo_pk)
            if class_form.is_valid():
                class_form.save()
                messages.success(request, f'update success')
        else:
            class_form= MenuButtonForm(instance=grupo_pk)
        data = {
            "user":user_name,
            "grupos": page_obj,
            "grupo_pk":grupo_pk,
            "form": class_form,
            "datas_extra": data2
        }
    else:
        if not request.user.is_authenticated:
            return redirect('login')
        return redirect('all_grup')

    return render(request, "view_menu/update_especies.html", data)
def Menu_add(request):
    if request.method =="POST":
        class_form = MenuButtonForm(request.POST,request.FILES)
        
        if class_form.is_valid():
            try: 
                __save =class_form.save()
                grupo_name = class_form.cleaned_data.get('titulo')
                Grupo=__save
                
                messages.success(request, f"add success ' {grupo_name} '")
                
                return redirect(f'select_Animals',Grupo.id_MenuButton)
            except :
                messages.success(request, 'Error En Los Datos Ingresado')
                return redirect('home_animals')
            
    else:
        class_form = MenuButtonForm()
    data = {
        "form": class_form
    }
    return render(request, "view_menu/form/form_add.html", data)
def Menu_delete(request, pk):
    try:
        class_grupo = MenuButton.objects.get(pk=pk)
    except MenuButton.DoesNotExist:
        messages.success(request, f'error delete')
        return redirect('select_Animals', pk)
    class_grupo.delete()
    messages.success(request, f"se a eliminado corectamente ' {class_grupo} '")
    return redirect('home_animals')




#Vista Informacion

def Informacion_home(request): 
    try: 
        menu_lista = MenuButton.objects.all()
        lista = Lista.objects.all()
        Infor = Informacion.objects.all()
        page_number = request.GET.get('page')
        paginatorInforma= Paginator(Infor, 12)
        
        page_obj = paginatorInforma.get_page(page_number)
        
        data= {
        "menu":menu_lista,
        "lista":lista,
        "groups": Infor,
        "pages":page_obj,
        }
        
    except Informacion.DoesNotExist:
        messages.success(request,'Error: la ruta no existe ')
        
    
    return render(request, "view_infor/all_view.html", data)
def add_Informacion(request,opc=str(), pk=0):
    type= opc if (opc in ('info_update','table','add')) and pk > 0 else False
    if not type:
       return redirect("select_informacion")
    
    if type== "info_update":
        #eseccion de info
        try:
            Info = Informacion.objects.get(pk=pk)
            tabla_r = Tabla.objects.filter(id_Info = Info.id)
            galeria = Galeria.objects.filter(id_Info=Info.id)
            
        except:
            pass
        
        if request.method =="POST":
            class_form = Informacion_form(request.POST)
            if class_form.is_valid():
                try: 
                    __save = class_form.save()
                    grupo_name = class_form.cleaned_data.get('nombre')
                
                    messages.success(request, f"update table success ' {grupo_name} '")
                    return redirect('addinformacion')
                
                except:
                    messages.success(request, 'Error Table not success')
                    return redirect('home_infor')
        else:
            class_form = Informacion_form(instance=Info)
        form_tables = [
            {
                "menu":MenuButton.objects.all(),#ERROR
                "lista":Lista.objects.all(),
                
            }
        ]
        
        data= {
        "Info": Info,
        "r_tabla":tabla_r,
        "r_galeria":galeria,
        "form": class_form,
        "form_ts":form_tables,
        "type":type
        
        }
        
        return render(request, 'view_infor/add_info/info.html', data)
    elif type =="table":
            #eseccion de table
        try:
            
            pass
        except:
            pass
        data= {
        
        "type":type
        
        }
        return render(request, 'view_infor/add_info/info.html', data)

    elif type== "add":
        try:
            
            pass
        except:
            pass
        return render(request, 'view_infor/add_info/info.html')


def Infor_home_add_tabla(request,pk=None):
   
    list_infor = Informacion.objects.all()
    list_table = Tabla.objects.all()
    search_table = request.GET.get("buscar_table")
    
    
    
    if list_infor.count() >= list_table.count() and list_table.count() != 0:
            color_text,status_color=("text-info","blue") 
    elif list_infor.count() == 0 or  list_table.count() == 0:
        color_text,status_color=("text-secondary","gray")
    else:
        color_text,status_color= ("text-danger","red")
   
        
    divisor = 0
    try: 
        divisor=   int((list_table / list_infor) *100)
    
        if divisor == 0:
            divisor = 100
    except: 
        divisor = 100
        
    if search_table:
        cliente = Tabla.objects.filter(
            Q(name__icontains= search_table)
             
        ).distinct()
        
        list_table= cliente if cliente else messages.success(request, f'No se encontro ({search_table}), Intentelo de nuevo ')
        
    
        
    dataclass = [{
        "tablas": list_table,
    }]
    table = [{
        "porcentual":divisor,
        "datos_inf":list_infor.count() ,
        "tablas": Tabla.objects.all().count(),
        "color_status" :status_color,
        "text_color": color_text,
        
        }]
    print(request.POST)
    if request.method =="POST":
        class_form = Form_table(request.POST)
        if class_form.is_valid():
            try: 
                __save = class_form.save()
                
                grupo_name = class_form.cleaned_data.get('name')
              
                messages.success(request, f"created table success ' {grupo_name} '")
                return redirect('addinformacion', 'table', __save.id)
            except:
                messages.success(request, 'Error Table not success')
                return redirect('home_infor')
    else:
        class_form = Form_table()
        
        print(class_form["id_Info"].value())
        
    data = {
        "form": class_form,
        "porcentaje": table,
        "tablas": dataclass,
        "s_infor":Informacion.objects.all(),
        "pk":pk
    }
    
    return render(request,"view_infor/view_tabla_infor.html", data) 

def Infor_home_del_tabla(request,pk):
    try:
        class_grupo = Tabla.objects.get(pk=pk)
    except Tabla.DoesNotExist:
        messages.success(request, f'error delete')
        return redirect('table_all_add',0)
    class_grupo.delete()
    messages.success(request, f"se a eliminado corectamente ' {class_grupo} '")
    return redirect('table_all_add',0)