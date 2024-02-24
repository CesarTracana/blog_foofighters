from django.contrib import admin
from .views import BlogDeleteView
from django.urls import path

urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name='post_delete'),
]