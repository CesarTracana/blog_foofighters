from .models import Post
from django.views.generic import ListView, TemplateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class HomePageView(ListView):
    model= Post  
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class BlogDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url= reverse_lazy("home")

class BlogCreateView(CreateView):
    model= Post
    template_name= "new_post.html"
    fields=["title", "body", "author"]

class BlogDetailView(DetailView):
    model=Post
    template_name="post_detail.html"

