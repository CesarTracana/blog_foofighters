from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView 
from .models import Post

def Hello (request): 
    return HttpResponse('Hello, World!')

class HomePageView(ListView):
    model= Post
    template_name="home.html"


class BlogCreateView(CreateView):
    model= Post
    template_name= "new_post.html"
    fields=["title", "text"]

class BlogCreateView(CreateView):
    model= Post
    template_name= "new_post.html"
    fields=["title", "text"]