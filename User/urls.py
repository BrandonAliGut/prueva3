from django.urls import path
from .views import *

urlpatterns = [
    path("createuser", Register, name="register" ),
    path("login", Inicio_de_sesion, name="login" ),
    path("logout", Logout.as_view(), name="logout" )
]