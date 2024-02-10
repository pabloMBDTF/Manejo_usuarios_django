from django import forms


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


    