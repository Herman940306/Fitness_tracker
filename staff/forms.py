"""
This module contains the form definitions for the Staff model in the
fitness_tracker application.

Preconditions:
- The `Staff` model must be defined in the `models.py` file
of the same application.
- The `Staff` model must have the fields `name`, `address`, and `date_of_birth`

Postconditions:
- The `StaffForm` class provides a form for creating and updating
`Staff` instances.
- The `date_of_birth` field in the form will render as an HTML date input.
"""
from django import forms
from .models import Staff


# Form for creating and updating Staff instances
class StaffForm(forms.ModelForm):
    ''' This form handles the creation and updating of Staff instances. '''
    class Meta:
        ''' This class defines the metadata for the form. '''
        model = Staff
        fields = ['name', 'address', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
