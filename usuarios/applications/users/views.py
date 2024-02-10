from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, View
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLogin
from .models import User



# Create your views here.


class CrearUser(FormView):
    template_name = "users/createUser.html"
    form_class = UserRegisterForm
    success_url = '/' 

    def form_valid(self, form):
       
        
        User.objects.create_user(
            form.cleaned_data['userName'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero']
        )
        return super().form_valid(form)
    

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = UserLogin
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
       
        user = authenticate(
            userName = form.cleaned_data['userName'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    
    
class LogoutView (View):
    
    def get (self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:loginUser')
        )