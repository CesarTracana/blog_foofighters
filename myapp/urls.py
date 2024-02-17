from django.contrib import admin
from .views import Hello, BlogCreateView
from django.urls import path

urlpatterns = [
    path ('', Hello, name="myapp"),
    path('crear/', BlogCreateView.as_view(), name='crear'),
    
]