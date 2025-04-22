from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkoutCategory, Exercise, WorkoutRoutine, FitnessGoal
from .forms import WorkoutCategoryForm, ExerciseForm, WorkoutRoutineForm, FitnessGoalForm

# Workout Category Views
@login_required
def category_list(request):
    categories = WorkoutCategory.objects.all()
    return render(request, 'fitness/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = WorkoutCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = WorkoutCategoryForm()
    return render(request, 'fitness/category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(WorkoutCategory, pk=pk)
    if request.method == 'POST':
        form = WorkoutCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = WorkoutCategoryForm(instance=category)
    return render(request, 'fitness/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(WorkoutCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'fitness/category_confirm_delete.html', {'category': category})

# Exercise Views
@login_required
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'fitness/exercise_list.html', {'exercises': exercises})

@login_required
def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'fitness/exercise_form.html', {'form': form})

@login_required
def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'fitness/exercise_form.html', {'form': form})

@login_required
def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('exercise_list')
    return render(request, 'fitness/exercise_confirm_delete.html', {'exercise': exercise})

# Workout Routine Views
@login_required
def workout_list(request):
    workouts = WorkoutRoutine.objects.all()
    return render(request, 'fitness/workout_list.html', {'workouts': workouts})

@login_required
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutRoutineForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.created_by = request.user
            workout.save()
            form.save_m2m()  # For many-to-many relationships
            return redirect('workout_list')
    else:
        form = WorkoutRoutineForm()
    return render(request, 'fitness/workout_form.html', {'form': form})

@login_required
def workout_update(request, pk):
    workout = get_object_or_404(WorkoutRoutine, pk=pk)
    if request.method == 'POST':
        form = WorkoutRoutineForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutRoutineForm(instance=workout)
    return render(request, 'fitness/workout_form.html', {'form': form})

@login_required
def workout_delete(request, pk):
    workout = get_object_or_404(WorkoutRoutine, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'fitness/workout_confirm_delete.html', {'workout': workout})

# Fitness Goal Views
@login_required
def goal_list(request):
    goals = FitnessGoal.objects.filter(user=request.user)
    return render(request, 'fitness/goal_list.html', {'goals': goals})

@login_required
def goal_create(request):
    if request.method == 'POST':
        form = FitnessGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = FitnessGoalForm()
    return render(request, 'fitness/goal_form.html', {'form': form})

@login_required
def goal_update(request, pk):
    goal = get_object_or_404(FitnessGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FitnessGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = FitnessGoalForm(instance=goal)
    return render(request, 'fitness/goal_form.html', {'form': form})

@login_required
def goal_delete(request, pk):
    goal = get_object_or_404(FitnessGoal, pk=pk, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('goal_list')
    return render(request, 'fitness/goal_confirm_delete.html', {'goal': goal})

@login_required
def progress_tracker(request):
    exercises = Exercise.objects.all()
    goals = FitnessGoal.objects.filter(user=request.user)
    return render(request, 'fitness/progress_tracker.html', {
        'exercises': exercises,
        'goals': goals
    })
    
def home(request):
    workouts = WorkoutRoutine.objects.all()[:5]  # Get first 5 workouts
    return render(request, 'fitness/home.html', {'workouts': workouts})
