from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('index/', views.IndexVista.as_view(), name = 'index'),
]