from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class StaffUser(AbstractUser):
    role = models.CharField(max_length=20)