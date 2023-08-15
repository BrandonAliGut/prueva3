from django import forms
from .models import *
from Api_grup_all.models import *
class Informacion_form(forms.ModelForm):
    Opc_tipo = [
                ("MenuButton","MenuButton"),
                ("Lista","Lista")
                ]
    nombre = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"add name"
            }
        )
    )
    texto = forms.CharField(
        required=False,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"..."
            }
        )
    )
    
    PGRUPO=forms.ModelChoiceField(
        required=False,
        queryset = MenuButton.objects.all(),
        widget=forms.Select(
           
            attrs={
                'class':'form-select',
                'id':'country',
            }
        )
    )
    
    PGRUPO_Lista=forms.ModelChoiceField(
        required=False,
        queryset = Lista.objects.all(),
        widget=forms.Select(
            attrs={
                'class':'form-select',
                'id':'country',
            }
        )
    )
    padre=forms.ChoiceField(
        required=True,
        choices=Opc_tipo,
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
        model = Informacion
        fields= (
            "__all__"
        )

    
class Form_table(forms.ModelForm):
    name = forms.CharField(
        required=True,
        min_length=2,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                'placeholder':"add name",
                'id':'name_campo'
            }
        )
    )
    id_Info=forms.ModelChoiceField(
        required=True,
        queryset = Informacion.objects.all(),
        
        widget=forms.Select(
           
            attrs={
                'class':'form-select',
                'id':'group',
                
            }
        )
    )
    def add(self, pk=0):
        if pk !=0:
            self.id_Info.queryset = Informacion.objects.get(id=pk)
    
    
    class Meta:
        model = Tabla
        fields= (
            "__all__"
        )
