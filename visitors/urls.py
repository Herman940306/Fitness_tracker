from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitor_list, name='visitor_list'),
    path('new/', views.visitor_create, name='visitor_create'),
    path('<int:pk>/edit/', views.visitor_update, name='visitor_update'),
    path('<int:pk>/delete/', views.visitor_delete, name='visitor_delete'),
]