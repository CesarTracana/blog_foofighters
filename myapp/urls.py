from django.contrib import admin
from .views import Hello, HomePageView
from django.urls import path
from .views import BlogCreateView

urlpatterns = [
    path ('', HomePageView.as_view(), name="home"),
    path('crear/', BlogCreateView.as_view(), name='crear'),
    
]


