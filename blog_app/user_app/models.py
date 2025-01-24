from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    description = models.TextField(max_length=512, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_app_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_app_users',
        blank=True
    )
    
    class Meta:
        pass