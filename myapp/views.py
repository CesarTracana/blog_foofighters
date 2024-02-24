from .models import Post
from django.views.generic import ListView, TemplateView, DeleteView
from django.urls import reverse_lazy

class HomePageView(ListView):
    model= Post  
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class BlogDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url= reverse_lazy("home")
