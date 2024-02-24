from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

def Hello (request): 
    return HttpResponse('Hello, World!')

class HomePageView(ListView):
    model= Post
    template_name="home.html"
