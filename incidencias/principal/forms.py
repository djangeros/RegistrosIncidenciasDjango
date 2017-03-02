#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from principal.models import Incidencia, Solucion, Cierre

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class IncidenciaForm(ModelForm):
    class Meta:
        model = Incidencia
        fields = '__all__'

class SolucionForm(ModelForm):
    class Meta:
        model = Solucion
        fields = '__all__'

class CierreForm(ModelForm):
	class Meta:
		model = Cierre
		fields = '__all__'

class EditarContrasenaForm(forms.Form):

    actual_password = forms.CharField(
        label='Contraseña actual',
        min_length=4,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        label='Nueva contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(
        label='Repetir contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2