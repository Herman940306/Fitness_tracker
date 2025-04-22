from django import forms
from .models import WorkoutCategory, Exercise, WorkoutRoutine, FitnessGoal

class WorkoutCategoryForm(forms.ModelForm):
    class Meta:
        model = WorkoutCategory
        fields = ['name']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'category', 'muscle_group', 'reps', 'sets']

class WorkoutRoutineForm(forms.ModelForm):
    class Meta:
        model = WorkoutRoutine
        fields = ['name', 'exercises']
        widgets = {
            'exercises': forms.CheckboxSelectMultiple,
        }

class FitnessGoalForm(forms.ModelForm):
    class Meta:
        model = FitnessGoal
        fields = ['description', 'target']