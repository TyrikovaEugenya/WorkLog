from django.db import models
from users.models import User
from projects.models import Project

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='time_entries')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='time_entries')
    hours = models.PositiveIntegerField()
    date = models.DateField()
    description = models.TextField(blank=True)
    objects = models.Manager()


