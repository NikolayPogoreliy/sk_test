from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    alias = models.CharField(max_length=10)


class Account(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=300)
