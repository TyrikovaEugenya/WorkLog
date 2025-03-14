from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('manager', 'Менеджер'),
        ('employee', 'Сотрудник'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='employee')
    objects = models.Manager()
    

