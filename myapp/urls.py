from django.contrib import admin
from .views import Hello
from django.urls import path

urlpatterns = [
    path ('', Hello, name="myapp")
]