from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    ROLES = (
        ('A', 'Admin'),
        ('M', 'Manager'),
        ('E', 'Employye'),
    )

    name = models.CharField('Name', max_length=15, default='')
    role = models.CharField('Role', max_length=1, choices=ROLES, default='')