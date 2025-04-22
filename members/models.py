"""
This module defines the Member model for the fitness tracker application.
"""
# Pre-conditions:
# - The `django.db` and `django.conf.settings` modules
# must be available and imported.
# - The `settings.AUTH_USER_MODEL` must be defined in the Django
# project settings.
# - The database must be properly configured and migrations applied.

# Post-conditions:
# - A `Member` model is defined with fields: `user`, `name`, `email`,
# `created_at`, `date_of_birth`, `address`, and `contact_number`.
# - The `Member` model is linked to the user model
# via a ForeignKey relationship.
# - The `__str__` method returns the `name` of the member.

from django.db import models
from django.conf import settings


# Create model for members of the fitness center
# models.py
class Member(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='members'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.name)
