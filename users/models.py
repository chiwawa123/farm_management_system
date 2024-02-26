from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from roles.models import Role

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email address'))
    is_active = models.BooleanField(default=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)  # Use PasswordField instead of CharField

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email