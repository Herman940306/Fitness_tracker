from django.db import models
from django.contrib.auth.models import AbstractUser


# Class to create roles for users
class CustomUser(AbstractUser):
    ROLES = (
        ('ADMIN', 'Admin'),
        ('STAFF', 'Staff'),
        ('VISITOR', 'Visitor'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='VISITOR')
