from django import forms
from django.contrib.auth.models import User
from .models import BeneficiarioCalentador, MUNICIPIOS


class BeneficiarioCalentadorForm(forms.ModelForm):

    class Meta:
        model = BeneficiarioCalentador
        fields = '__all__'

        widgets = {
            'folio_mids': forms.NumberInput(attrs={'class':'form-control','placeholder':'Folio MIDS'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido Paterno'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido Materno'}),
            'nombres': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre(s)'}),
            'localidad': forms.TextInput(attrs={'class':'form-control','placeholder':'Localidad'}),
        }
    
    designado = forms.ModelChoiceField(queryset=User.objects.all(), label="Designado", widget=forms.Select(attrs={"class": "form-control", "placeholder":"Designado"}))
    municipio = forms.ChoiceField(label="Municipio", choices=MUNICIPIOS, widget=forms.Select(attrs={"class": "form-control", "placeholder":"Municipio"}))
