from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

class SuperuserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'full_name']


class EditUserForm(UserChangeForm):
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))
    first_name = forms.CharField(label='Nombre/s', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre/s'}))
    last_name = forms.CharField(label='Apellido/s', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Apellido/s'}))
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}))
    password = forms.CharField(
        label='', widget=forms.TextInput(attrs={'type': 'hidden'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Contraseña Actual"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': "form-control",
                "autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = forms.CharField(
        label=("Nueva Contraseña"),
        widget=forms.PasswordInput(
            attrs={'class': "form-control", "autocomplete": "new-password"}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=("Confirme la nueva Contraseña"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': "form-control", "autocomplete": "new-password"}),
    )
    field_order = ["old_password", "new_password1", "new_password2"]