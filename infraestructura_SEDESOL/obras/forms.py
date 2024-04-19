from django import forms
from django.contrib.auth.models import User
from .models import ObraPublica, MUNICIPIOS

class ObraPublicaForm(forms.ModelForm):
    class Meta:
        model = ObraPublica
        fields = '__all__'

        widgets = {
            'folio_mids': forms.NumberInput(attrs={'class':'form-control','placeholder':'Folio MIDS'}),
            'nombre_obra': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de la obra'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Descripcion'}),
            'localidad': forms.TextInput(attrs={'class':'form-control','placeholder':'Localidad'}),
        }
    
    designado = forms.ModelChoiceField(queryset=User.objects.all(), label="Designado", widget=forms.Select(attrs={"class": "form-control","placeholder":"Designado"}))
    municipio = forms.ChoiceField(label="Municipio", choices=MUNICIPIOS, widget=forms.Select(attrs={"class": "form-control", "placeholder":"Municipio"}))

class FiltroObraPublicaForm(forms.Form):
    municipio = forms.ChoiceField(
        required=False,
        choices = tuple([(u'', "Todos")] + MUNICIPIOS),
        widget = forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    nombre_obra = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        required=False
    )
    localidad = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Localidad'}),
        required=False
    )
    folio_mids = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Folio'}),
        required=False
    )