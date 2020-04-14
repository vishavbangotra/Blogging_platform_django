from django.shortcuts import render
from django.views.generic import ListView, DetailView, DetailView, CreateView, UpdateView, TemplateView
from blog.models import Comments, Post

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.object.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(CreateView):
    model = Post
    
