from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    

    def _createUser(self, userName, email, password, is_staff, is_superuser, **extraFields):
        user = self.model(
            userName = userName,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extraFields
        )
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_user(self, userName, email, password = None, **extraFields):
        return self._createUser(userName, email, password, False, False, **extraFields)

    def create_superuser(self, userName, email, password = None, **extraFields):
        return self._createUser(userName, email, password, True, True, **extraFields)