from django.contrib import admin
from .views import Hello, BlogDeleteView
from django.urls import path

urlpatterns = [
    path ('', Hello, name="myapp"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name='post_delete')
]