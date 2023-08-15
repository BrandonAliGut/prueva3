from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from .baseview import *
from .view_index import index
#index home
urlpatterns = [
    path("",index, name="home"),
    
]
# page group all
urlpatterns += [
    path("Home_page", Admin_page_home.as_view(), name="home_grupo"),
    path("Home_page_animals", Admin_page_animales_grupos.as_view(), name="home_animals_grupo"),
    path("Home_page_animal_menu", Admin_page_animales_menu.as_view(), name="home_animals"),
    path("Home_page_Informacion", Admin_page_animales_Informacion.as_view(), name="home_infor"),#informacion
    
    path("Home_page_info", Admin_page_animales_grupos.as_view(), name="home_info"),
]
#add grupos de especies 
urlpatterns +=[
    path("admin-especies/<int:pk>", group_Especies, name="select_species"),
    path("admin-especies/add", Especie_add, name="add_especies"),
    path("admin_especies_del/<int:pk>", Especie_delete, name="especies_delete")
    
]

#add grupos de Animales o menu
urlpatterns +=[
    path("admin_animals/<int:pk>", group_Menu, name="select_Animals"),
    path("admin_animals/add", Menu_add, name="add_Animals"),
    path("admin_animals_del/<int:pk>", Menu_delete, name="animal_delete")
]
#add Informacion las especies y enfermedades add_Informacion
urlpatterns += [
    path("admin_Informacion", Informacion_home, name="select_informacion"),
    path("addInformacion/<str:opc>/<int:pk>", add_Informacion, name="addinformacion"),
    
    path("add_table/<int:pk>", Infor_home_add_tabla, name="table_all_add"),
    path("del_table/<int:pk>", Infor_home_del_tabla, name="table_del"),
]


# add Group urls
urlpatterns += [
    path("admin-app", group_admin, name="admin_home"),
    path("admin-app/<int:pk>", group_admin, name="select_grup"),
    path("admin-grup", Page_grup.as_view(), name="all_grup"),
    path("admin_form/<int:pk>", group_admin, name="admin_grup_form"),
    path("admin_form_del/<int:pk>", grup_delete, name="admin_grup_delete"),
    path("add_grupo", grup_add, name="add_grup"),
]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)