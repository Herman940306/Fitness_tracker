"""
This module defines the models for the staff members of the fitness center.
It includes the Staff model with fields for name, address, date of birth,
and timestamps for creation and updates.
"""
from django.db import models


# Create model for staff members of the fitness center
class Staff(models.Model):
    '''Staff member model for the fitness center'''
    name = models.CharField(max_length=100)
    address = models.TextField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
