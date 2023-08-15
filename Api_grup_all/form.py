from django import forms
from .models import *
from Pagos_zooapp_items.models import *

class GrupForm(forms.ModelForm):
    
    grupo = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"add Grupos"
            }
        )
    )
    activo = forms.BooleanField(required=False,widget=forms.CheckboxInput(
        attrs={
            'class': "form-check-input",
            'type':'checkbox',
            'id': 'inlineCheckbox1'
        }
    ))
    class Meta:
        model = GrupoAnimals
        fields= (
            "__all__"
        )



class GrupEspecies(forms.ModelForm):
    
    AnimalList = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"add Grupos"
            }
        )
    )
    PGRUPO=forms.ModelChoiceField(
        required=False,
        queryset = GrupoAnimals.objects.all(),
        widget=forms.Select(
           
            attrs={
                'class':'form-select',
                'id':'country',
            }
        )
    )
    Id_Categoria=forms.ModelChoiceField(
        required=False,
        queryset = Nivel_Informacion_base.objects.all(),
        widget=forms.Select(
            
            attrs={
                'class':'form-select',
                'id':'country',
            }
        )
    )
    activo = forms.BooleanField(required=False,widget=forms.CheckboxInput(
        attrs={
            'class': "form-check-input",
            'type':'checkbox',
            'id': 'inlineCheckbox1'
        }
    ))
    class Meta:
        model = ListAnimalGrupos
        fields= (
            "__all__"
        )

class MenuButtonForm(forms.ModelForm):
    Opc_tipo = [
                ('A', 'Menu'),
                ('B', 'Directo'),
                ]
    titulo = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"add titulo"
            }
        )
    )
    opcion=forms.ChoiceField(
        required=True,
        choices=Opc_tipo,
        widget=forms.Select(
            
            attrs={
                'class':'form-select',
                'id':'country',
            }
        )
    )
    
    PGRUPO=forms.ModelChoiceField(
        required=False,
        queryset = ListAnimalGrupos.objects.all(),
        widget=forms.Select(
           
            attrs={
                'class':'form-select',
                'id':'country',
            }
        )
    )
    Id_Categoria=forms.ModelChoiceField(
        required=False,
        queryset = Nivel_Informacion_base.objects.all(),
        widget=forms.Select(
            
            attrs={
                'class':'form-select',
                'id':'country',
            }
        )
    )
    activo = forms.BooleanField(required=False,widget=forms.CheckboxInput(
        attrs={
            'class': "form-check-input",
            'type':'checkbox',
            'id': 'inlineCheckbox1'
        }
    ))
    class Meta:
        model = MenuButton
        fields= (
            "__all__"
        )

