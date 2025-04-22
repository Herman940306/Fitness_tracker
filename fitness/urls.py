from django.urls import path
from . import views

urlpatterns = [
    
    # Home Page
    path('', views.home, name='home'),
    
    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # Exercises
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('exercises/new/', views.exercise_create, name='exercise_create'),
    path('exercises/<int:pk>/edit/', views.exercise_update, name='exercise_update'),
    path('exercises/<int:pk>/delete/', views.exercise_delete, name='exercise_delete'),
    
    # Workout Routines
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/new/', views.workout_create, name='workout_create'),
    path('workouts/<int:pk>/edit/', views.workout_update, name='workout_update'),
    path('workouts/<int:pk>/delete/', views.workout_delete, name='workout_delete'),
    
    # Fitness Goals
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/new/', views.goal_create, name='goal_create'),
    path('goals/<int:pk>/edit/', views.goal_update, name='goal_update'),
    path('goals/<int:pk>/delete/', views.goal_delete, name='goal_delete'),
    
    # Progress Tracking
    path('progress/', views.progress_tracker, name='progress_tracker'),
]