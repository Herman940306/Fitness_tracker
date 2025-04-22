from django.db import models
from visitors.models import Visitor
from staff.models import Staff


# Create model for visits to the fitness center

class Visit(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    visit_date = models.DateTimeField()
    purpose = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.visitor.name} - {self.visit_date}"
