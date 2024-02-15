from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_regularuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    tasks = models.ManyToManyField('taskmanager.Task', related_name='assigned_tasks', blank=True)

    def __str__(self):
        return self.username