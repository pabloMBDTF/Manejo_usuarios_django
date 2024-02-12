from django.db import models
from .manager import UserManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class User (AbstractBaseUser, PermissionsMixin):

    GENDER_CHOISES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('G', 'Gay'),
    )

    userName = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(unique = True)
    nombres = models.CharField(max_length = 50, blank = True)
    apellidos = models.CharField(max_length = 50, blank = True)
    genero = models.CharField(max_length = 1, choices = GENDER_CHOISES, blank = True)
    codregistro = models.CharField(max_length = 6, default = '000000', blank = True)
    
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(blank = True, default = False)

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    USERNAME_FIELD = 'userName'
