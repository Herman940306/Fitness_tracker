from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('new/', views.staff_create, name='staff_create'),
    path('<int:pk>/edit/', views.staff_update, name='staff_update'),
    path('<int:pk>/delete/', views.staff_delete, name='staff_delete'),
]