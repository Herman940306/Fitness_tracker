from django.urls import path
from . import views

urlpatterns = [
    path('', views.visit_list, name='visit_list'),
    path('new/', views.visit_create, name='visit_create'),
    path('<int:pk>/edit/', views.visit_update, name='visit_update'),
    path('<int:pk>/delete/', views.visit_delete, name='visit_delete'),
]