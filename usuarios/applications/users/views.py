from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserRegisterForm
from .models import User



# Create your views here.


class CrearUser(CreateView):
    template_name = "users/createUser.html"
    form_class = UserRegisterForm
    success_url = '/' 
