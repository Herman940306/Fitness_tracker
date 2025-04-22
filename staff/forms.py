from django import forms
from .models import Staff


# Form for creating and updating Staff instances
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'address', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }