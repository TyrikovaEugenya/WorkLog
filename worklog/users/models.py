from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('manager', 'Менеджер'),
        ('employee', 'Сотрудник'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='employee')
    objects = models.Manager()
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Уникальное имя для обратного доступа
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Уникальное имя для обратного доступа
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    

