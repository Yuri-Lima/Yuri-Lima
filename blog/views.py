from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import Http404
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView 
from .models import Post
from users.models import Profile
from django.urls import reverse

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all(),
        'Profile': Profile.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostLisView(ListView):
    model: Post
    template_name = 'blog/home.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #{% for post in posts %}
    

    def get_queryset(self):
        return Post.objects.all().order_by('-date_posted')

#https://stackoverflow.com/questions/50497871/django-get-id-of-posted-form-in-post-method-of-view-that-contains-list-of-form
class PostDetailView(DetailView):
    model: Post # blog/post_detail.html
    template_name = 'blog/post_detail.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'post'

    def get_object(self, queryset=None): #https://levelup.gitconnected.com/django-quick-tips-get-absolute-url-1c22321f806b
        return Post.objects.get(pk=self.kwargs.get("pk"))

class PostCreateView(CreateView):
    model: Post
    fields = ['title', 'content', 'url','contact_number']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):#"""If the form is valid, save the associated model."""
        user = get_user_model()
        print('self.request.user:',self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Post.objects.all()
    # def get_object(self, queryset=None): 
    #     return Post.objects.get(pk=self.kwargs.get("pk"))


def about(request):
    return render(request, 'blog/about.html')


    # def detail(request, post_id):
    #     try:
    #         post = Post.objects.get(pk=post_id)
    #     except Post.DoesNotExist:
    #         raise Http404("Question does not exist")

    #     return render(request, 'post_detail.html', {'post': post})