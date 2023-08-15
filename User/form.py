from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model, authenticate

class RegisterForm(UserCreationForm):
    name= forms.CharField(
        required=True,
        widget=forms.TextInput(
            
            attrs={
                'placeholder':"Escriba su nombre",
                'class':"form-control"
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget= forms.TextInput(
            
            attrs={
                'type':'email',
                'class':"form-control",
                'id':'staticEmail',
                'placeholder':'Ingrese Su correo electronico'
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            
            attrs={
                'type':'password',
                'class':'form-control',
                'id':'inputPassword',
                'placeholder':'Contracena'
            }
        )
    )
    password2 = forms.CharField(
        min_length=8,
        required=True,
        label="Confirma Contraceña",
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'class':'form-control',
                'id':'inputPassword',
                'placeholder':'Comfirmar Contracena'
            }
        )
    )
    class Meta:
        model= get_user_model()
        fields=(
            'name',
            'email',
            'password1',
            'password2'
        )

class UserLoginForm(forms.Form):
    username= forms.CharField(
        required=True,
        widget=forms.TextInput(
            
            attrs={
                'placeholder':"Escriba su nombre",
                'class':"form-control"
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        min_length=1,
        required=True,
        widget=forms.PasswordInput(
            
            attrs={
                'type':'password',
                'class':'form-control',
                'id':'inputPassword',
                'placeholder':'Contracena'
            }
        )
    )

