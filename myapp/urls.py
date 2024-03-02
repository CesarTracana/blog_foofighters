from django.contrib import admin
from .views import Hello, HomePageView
from django.urls import path
from .views import BlogCreateView
from .views import BlogDetailView

urlpatterns = [
    path ('', HomePageView.as_view(), name="home"),
    path('crear/', BlogCreateView.as_view(), name='post_new'),
    path("detail/<int:pk>", BlogDetailView.as_view(), name= 'post_detail')

]


