from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView

def Hello (request): 
    return HttpResponse('Hello, World!')

class BlogDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url= reverse_lazy("home")
