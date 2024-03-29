from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
# Create your views here.


from django.views.generic import TemplateView



class IndexVista(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy = ('users_app:loginUser')
