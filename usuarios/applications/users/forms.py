from django import forms


from .models import User

class UserRegisterForm(forms.ModelForm):
    """UserRegisterForm definition."""

    # TODO: Define form fields here
    
    class Meta:
        model = User
        fields = '__all__'
