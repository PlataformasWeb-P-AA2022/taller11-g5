from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese un nombre por favor")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data['direccion']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese su direccion por favor")
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        palabra = valor.split()
        inicial = palabra[0]

        if inicial == "L":
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo_departamento', 'numero_cuartos']

    def clean_nombre(self):
        valor = self.cleaned_data['nombre_propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("El nombre completo de un propietario no debe tener menos de 3 palabras.")
        return valor  

    def clean_costo(self):
        valor = self.cleaned_data['costo_departamento']
        if(valor > 100000):
            raise forms.ValidationError("Costo de un departamento no puede ser mayor a $100 mil.")
        return valor

    def clean_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']
        if valor > 0 and valor < 7:
            raise forms.ValidationError("Número de cuartos no puede ser 0, ni mayor a 7")
        return valor


class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo_departamento', 'numero_cuartos']
