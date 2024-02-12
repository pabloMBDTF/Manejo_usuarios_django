from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, View
from django.views.generic.edit import FormView

from applications.users.functions import codeGenerator
from .forms import UserRegisterForm, UserLogin, UserUpdatePassword, ComfirmarEmail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User



# Create your views here.


class CrearUser(FormView):
    template_name = "users/createUser.html"
    form_class = UserRegisterForm
    success_url = '/' 

    def form_valid(self, form):
        #Generamos un codigo aleatorio de size = 6 entre letras y numeros
        codigo = codeGenerator()
        usuario = User.objects.create_user(
            form.cleaned_data['userName'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            codregistro = codigo
        )

        asunto = 'Confirmacion de email'
        mensaje = 'Codigo de verificacion' + codigo
        email_remitente = 'pablo.becerra@correounivalle.edu.co'
        send_mail(asunto, mensaje,email_remitente, [form.cleaned_data['email'],])
        # una vez que se confirme que se redirija
        return HttpResponseRedirect(
            reverse(
                'users_app:verificarCodigo',
                kwargs = {
                    'pk': usuario.id
                }
            )
        )
    

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
    

class UpdatePassword(LoginRequiredMixin, FormView):
    template_name = 'users/updatePassword.html'
    form_class = UserUpdatePassword
    success_url = reverse_lazy('users_app:loginUser')
    login_url = reverse_lazy = ('users_app:loginUser')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            userName = usuario.userName,
            password = form.cleaned_data['password1']
        )
        if user:
            usuario.set_password(form.cleaned_data['password2'])
            usuario.save()


        logout(self.request)
        return super(UpdatePassword, self).form_valid(form)
    

class verificarCodigo(FormView):
    template_name = 'users/confirmarCodigo.html'
    form_class = ComfirmarEmail
    success_url = reverse_lazy('users_app:loginUser')
    #login_url = reverse_lazy = ('users_app:loginUser')

    def get_form_kwargs(self) :
        kwargs = super(verificarCodigo, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk']
            }
        )
        return kwargs
        

    def form_valid(self, form):
        
        return super(verificarCodigo, self).form_valid(form)