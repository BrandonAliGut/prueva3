from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib import messages


from .form import *
# Create your views here.


def Register(request):
    
    template_name= 'User_Register/createUser.html'
    if request.method =="POST":
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password= form.cleaned_data.get('password1')
            user =authenticate(request,username=email, password=password)
            if user is not None:
                login(request,user)
            return (redirect('home'))
    else:
        form = RegisterForm
    
    return render(request, 'User_Register/createUser.html',{'form':form})

        

def Inicio_de_sesion(request):
    if request.method =="POST":
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password1')
            user =authenticate(request,username=usuario, password=password)
            if user is not None:
                login(request,user)
                if request.user.is_superuser:
                    messages.success(request, f'Bienvenido admin {request.user}')
                    return redirect('home')
                return redirect('home')
                
            elif user == None:
                messages.success(request, f'No existe el usuario incresado /n si no posee un usuario cree uno')
            
            return redirect('login')
    else:
        form = UserLoginForm
    
    return render(request, 'User_Register/loginview.html',{'form':form})

class Logout(LogoutView):
    template_name= "index_tem/index.html"