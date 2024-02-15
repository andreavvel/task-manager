from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_regularuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    #rn we use the is regular user bool to check which user is which
