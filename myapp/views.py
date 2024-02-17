from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView 
from .models import Post

def Hello (request): 
    return HttpResponse('Hello, World!')

class BlogCreateView(CreateView):
    model= Post
    template_name= "new_post.html"
    fields=["title", "text"]