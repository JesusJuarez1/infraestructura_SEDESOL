from django import forms
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
    
    municipio = forms.ChoiceField(label="Municipio", choices=MUNICIPIOS, widget=forms.Select(attrs={"class": "form-control"}))
