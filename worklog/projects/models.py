from django.db import models
from ..users.models import User


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=250)
    manager = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='managed_project')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
