from django.contrib import admin
from .views import BlogDeleteView
from django.urls import path
from .views import BlogCreateView, HomePageView
from .views import BlogDetailView 

urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name='post_delete'),
    path ('', HomePageView.as_view(), name="home"),
    path('crear/', BlogCreateView.as_view(), name='post_new'),
    path("detail/<int:pk>", BlogDetailView.as_view(), name= 'post_detail')

]


