from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WorkoutCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(WorkoutCategory, on_delete=models.CASCADE)
    muscle_group = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WorkoutRoutine(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FitnessGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    target = models.IntegerField()
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def progress_percentage(self):
        return (self.progress / self.target) * 100 if self.target > 0 else 0