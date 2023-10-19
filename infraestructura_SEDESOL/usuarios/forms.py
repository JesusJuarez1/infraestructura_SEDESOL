from django import forms
from .models import Beneficiarios_Calentadores

class BeneficiariosCalentadoresForm(forms.ModelForm):
    class Meta:
        model = Beneficiarios_Calentadores
        fields = '__all__'

        widgets = {
            'folio_mids': forms.NumberInput(attrs={'class':'form-control','placeholder':'Folio MIDS'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido Paterno'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido Materno'}),
            'nombres': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre(s)'}),
            'municipio': forms.TextInput(attrs={'class':'form-control','placeholder':'Municipio'}),
            'localidad': forms.TextInput(attrs={'class':'form-control','placeholder':'Localidad'}),
        }