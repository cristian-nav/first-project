from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs/', views.index),
    path('blogs/new/', views.new),
    path('blogs/create/', views.create),
    path('blogs/<_number>/', views.show),
    path('blogs/<_number>/edit/', views.edit),
    path('blogs/json/', views.json),
]