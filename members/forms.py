'''
# Pre-condition reasoning:
The MemberForm class is designed to handle the creation and updating of
Member instances.

It assumes that the Member model exists and has fields: name, address,
date_of_birth, contact_number, and email.

The form expects valid input for these fields, with specific widgets,
labels, help texts, and error messages defined.

# Post-condition reasoning:
After the form is instantiated and validated, it will provide cleaned data
for creating or updating a Member instance.

If the form is invalid, it will return appropriate error messages for the
user to correct their input.

The form ensures that the data adheres to the constraints and requirements
defined in the Member model and the form itself.'''

from django import forms
from .models import Member


# Form for creating and updating Member instances
class MemberForm(forms.ModelForm):
    ''' This form handles the creation and updating of Member instances. '''
    class Meta:
        ''' This class defines the metadata for the form. '''
        model = Member
        fields = ['name',
                  'address',
                  'date_of_birth',
                  'contact_number',
                  'email'
                  ]
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
            'name': 'Enter the full name of the member.',
            'address': 'Enter the address of the member.',
            'date_of_birth': 'Select the date of birth of the member.',
            'contact_number': 'Enter the contact number of the member.',
            'email': 'Enter a valid email address for the member.',
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
