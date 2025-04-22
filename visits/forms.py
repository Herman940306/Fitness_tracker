from django import forms
from .models import Visit
from visitors.models import Visitor
from staff.models import Staff

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
