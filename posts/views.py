from audioop import reverse
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView ,DetailView,DeleteView

from posts.models import BlogPost

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class blogHome(ListView):
    model= BlogPost
    context_object_name="posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

@method_decorator(login_required,name='dispatch')
class BlogPostCreate(CreateView):
    model= BlogPost
    template_name="posts/blogpost_create.html"
    fields= ['title','content',]

class BlogPostUpdate(UpdateView):
    model= BlogPost
    template_name="posts/blogpost_update.html"
    fields= ['title','content','published']

class BlogPostDetail(DetailView):
    model= BlogPost
    context_object_name="post"

class BlogPostDelete(DeleteView):
    model= BlogPost
    success_url=reverse_lazy("posts:home")
    context_object_name="post"
