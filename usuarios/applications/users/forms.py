from django import forms

from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    """UserRegisterForm definition."""

    password1 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Repetir contraseña'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'userName',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    
   
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son las mismas.')
        elif (len(self.cleaned_data['password1']) < 5):
            self.add_error('password1', 'Las contraseñas deben de tener de 5 dijitos en adelante ')
                

class UserLogin(forms.Form):
    
    userName = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )

    def clean(self):
        cleaned_data = super(UserLogin, self).clean()
        username = self.cleaned_data['userName']
        password = self.cleaned_data['password']

        if not authenticate(username = username, password = password):
            raise forms.ValidationError('Los datos de el usuario no se han podido validar.')
        
        return self.cleaned_data
    

class UserUpdatePassword(forms.Form):
    password1 = forms.CharField(
        label = 'Contraseña actual',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña nueva',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Repetir contraseña'
            }
        )
    )


class ComfirmarEmail(forms.Form):
    codRegistro = forms.CharField(required = True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(ComfirmarEmail, self).__init__(*args, **kwargs)

    def clean_codRegistro(self):
        codigo = self.cleaned_data['codRegistro']

        if len(codigo) == 6:
            #verifiacmos si el codigo y el id son validos
            activo = User.objects.codeValidation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('el codigo es invalido.')
        else:
            raise forms.ValidationError('el codigo es invalido.')