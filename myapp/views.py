from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class UpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
