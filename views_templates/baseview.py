from django.shortcuts import render, redirect

from Api_grup_all.models import *
from Api_grup_all.form import *
from Infor_table_more.form import *
from Infor_table_more.models import *




from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin



class Admin_page_home(PermissionRequiredMixin,ListView):
    permission_required= (
        'Api_grup_all.view_grupoanimals'
    )
    template_name= "page_all/lis_groups.html"
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
                "select":'bg-success'
                }
                return render(request, "page_all/lis_groups.html", data)
            except GrupoAnimals.DoesNotExist:
                messages.success(request,'Error: la ruta no existe ')
                return redirect('home')
        return redirect('home')
    
class Admin_page_animales_grupos(PermissionRequiredMixin,ListView):
    permission_required= (
        'Api_grup_all.view_grupoanimals'
    )
    template_name= "page_all/list_animals_group.html"
    model = ListAnimalGrupos
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try: 
                grupoanimals = GrupoAnimals.objects.all()
                grupo = ListAnimalGrupos.objects.all()
                page_number = request.GET.get('page')
                paginator= Paginator(grupo, 12)
                
                page_obj = paginator.get_page(page_number)
                
                data= {
                "grupos": grupo,
                "pages":page_obj,
                "grupoAnimalas":grupoanimals
                }
                return render(request, "page_all/list_animals_group.html", data)
            except ListAnimalGrupos.DoesNotExist:
                messages.success(request,'Error: la ruta no existe ')
                return redirect('home')
        return redirect('home')

class Admin_page_animales_menu(PermissionRequiredMixin,ListView):
    permission_required= (
        'Api_grup_all.view_grupoanimals'
    )
    template_name= "page_all/list_animal_menu.html"
    model = MenuButton
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try: 
                lista = ListAnimalGrupos.objects.all()
                grupo = MenuButton.objects.all()
                page_number = request.GET.get('page')
                paginatormenu= Paginator(grupo, 12)
                
                page_obj = paginatormenu.get_page(page_number)
                
                data= {
                "grupos": grupo,
                "lista_All": lista,
                "pages":page_obj,
                
                }
                return render(request, "page_all/list_animal_menu.html", data)
            except MenuButton.DoesNotExist:
                messages.success(request,'Error: la ruta no existe ')
                return redirect('home')
        return redirect('home')

class Admin_page_animales_Informacion(PermissionRequiredMixin,ListView):
    permission_required= (
        'Api_grup_all.view_grupoanimals'
    )
    template_name= "page_all/list_animals_Informacion.html"
    model = Informacion
    def all_info(self, request, *args, **kwargs):
        try: 
            Infor = Informacion.objects.all()
            page_number = request.GET.get('page')
            paginatorInforma= Paginator(Infor, 12)
            
            page_obj = paginatorInforma.get_page(page_number)
            
            data= {
            "groups": Infor,
            "pages":page_obj,
            }
            return data
        except Informacion.DoesNotExist:
            messages.success(request,'Error: la ruta no existe ')
            return {}
                
        
    def add_table(self, request, *args, **kwargs):
        self.save_instace = None
        if request.method =="POST":
            class_form = Form_table(request.POST)
            
            if class_form.is_valid():
                try: 
                    __save = class_form.save()
                 
                    grupo_name = class_form.cleaned_data.get('name')
                    class_form = Form_table()
                    messages.success(request, f"created table success ' {grupo_name} '")
                    
                except:
                    messages.success(request, 'Error Table not success')
                    return redirect('home_infor')
        else:
            class_form = Form_table()
        data = {
            "form": class_form,
            
            
        }
        
        return data
    
    def galeria(self, request, *args, **kwargs):
        return {}
    
    def dispatch(self, request, *args, **kwargs):
        print(self.all_info(request, *args, **kwargs))
        json_def_data = {
                "all":self.all_info(request, *args, **kwargs),
                "add_table": self.add_table(request, *args, **kwargs),
                "galeria":[self.galeria(request, *args, **kwargs)],
            }
        
        return render(request, "page_all/list_animals_Informacion.html", json_def_data)
        





"""
class IndexView(ListView):
    context_object_name = 'home_list'    
    template_name = 'contacts/index.html'
    queryset = Individual.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        context['venue_list'] = Venue.objects.all()
        context['festival_list'] = Festival.objects.all()
        # And so on for more models
        return context"""