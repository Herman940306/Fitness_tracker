"""
This module defines the Visit model for tracking visits to the fitness center.
Classes:
    Visit: Represents a visit to the fitness center by a member, optionally
assisted by a staff member.
Preconditions:
    - The `Member` model must exist in the `members` app.
    - The `Staff` model must exist in the `staff` app.
    - The database must be properly configured to store the Visit model.
Postconditions:
    - Instances of the Visit model can be created,
    retrieved, updated, and deleted.
    - Each Visit instance will be associated with
    a Member and optionally a Staff member.
    - Visit instances will store the visit date and purpose of the visit.
"""
from django.db import models
from members.models import Member
from staff.models import Staff


# Create model for visits to the fitness center

class Visit(models.Model):
    ''' This model represents a visit to the fitness center by a member. '''
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='visits'
    )
    staff = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    visit_date = models.DateTimeField()
    purpose = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.member.name} - {self.visit_date}"
