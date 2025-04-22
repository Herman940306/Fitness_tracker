''' This module contains forms for handling Visit instances
in the fitness tracker application. '''
from django import forms
from .models import Visit


# Form for creating and updating Visit instances
class VisitForm(forms.ModelForm):
    ''' This form handles the creation and updating of Visit instances. '''
    class Meta:
        model = Visit
        fields = '__all__'
