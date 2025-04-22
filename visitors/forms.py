from django import forms
from .models import Visitor


# Form for creating and updating Visitor instances
class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'address', 'date_of_birth', 'contact_number', 'email']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Visitor Name',
            'address': 'Address',
            'date_of_birth': 'Date of Birth',
            'contact_number': 'Contact Number',
            'email': 'Email Address',
        }
        help_texts = {
            'name': 'Enter the full name of the visitor.',
            'address': 'Enter the address of the visitor.',
            'date_of_birth': 'Select the date of birth of the visitor.',
            'contact_number': 'Enter the contact number of the visitor.',
            'email': 'Enter a valid email address for the visitor.',
        }
        error_messages = {
            'name': {
                'max_length': "This name is too long.",
                'required': "This field is required.",
            },
            'email': {
                'invalid': "Enter a valid email address.",
                'required': "This field is required.",
            },
            'contact_number': {
                'max_length': "This contact number is too long.",
                'required': "This field is required.",
            },

        }
