from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView



class IndexVista(TemplateView):
    template_name = "home/index.html"
