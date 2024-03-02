from django.contrib import admin
from .views import HomePageView, UpdateView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path("post/<int:pk>/edit/", UpdateView.as_view(), name='post_edit'),
]
