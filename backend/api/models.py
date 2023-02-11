from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.contrib.auth import get_user, get_user_model

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=50)
    userTask = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title