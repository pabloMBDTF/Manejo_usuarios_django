
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.CrearUser.as_view(), name = 'registerUser'),
    path('login/', views.LoginUser.as_view(), name = 'loginUser'),
    path('logout/', views.LogoutView.as_view(), name = 'logoutUser'),
    path('UpdatePassword/', views.UpdatePassword.as_view(), name = 'UpdatePassword'),
    path('confirmarCodigo/<pk>/', views.verificarCodigo.as_view(), name = 'verificarCodigo'),
]