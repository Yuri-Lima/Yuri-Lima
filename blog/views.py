from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404)
from django.views.generic import (
    CreateView, 
    ListView, 
    UpdateView, 
    DeleteView, 
    DetailView )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Post
from users.models import Profile
from django.urls import reverse

# Create your views here.
# def home(request):
#     context = {
#         'posts':Post.objects.all(),
#         'Profile': Profile.objects.all(),
#     }
#     return render(request, 'blog/home.html', context)

class PostLisView(ListView):
    model: Post
    template_name = 'blog/home.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #{% for post in posts %}
    paginate_by = 5 #the number of posts per page 
    

    def get_queryset(self):
        return Post.objects.all().order_by('-date_posted')

#https://stackoverflow.com/questions/50497871/django-get-id-of-posted-form-in-post-method-of-view-that-contains-list-of-form
class PostDetailView(DetailView):
    model: Post # blog/post_detail.html
    template_name = 'blog/post_detail.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'post'

    def get_object(self, queryset=None): #https://levelup.gitconnected.com/django-quick-tips-get-absolute-url-1c22321f806b
        return Post.objects.get(pk=self.kwargs.get("pk"))

class PostCreateView(LoginRequiredMixin,CreateView):
    model: Post
    fields = ['title', 'content', 'url','contact_number']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):#"""If the form is valid, save the associated model."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Post.objects.all()
    # def get_object(self, queryset=None): 
    #     return Post.objects.get(pk=self.kwargs.get("pk"))

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model: Post
    fields = ['title', 'content', 'url','contact_number']
    # template_name = 'blog/post_form.html'
    
    def form_valid(self, form):#"""If the form is valid, save the associated model."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Post.objects.all()

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):#respect those postions
    model = Post
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserPostLisView(ListView):
    model: Post
    template_name = 'blog/user_posts.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #{% for post in posts %}
    paginate_by = 5 #the number of posts per page 

    def get_queryset(self):
        getUser = get_user_model()
        user = get_object_or_404(getUser, username=self.kwargs.get('username')) #Ele pega o user que vem pela URL
        return Post.objects.filter(author=user).order_by('-date_posted')



def about(request):
    return render(request, 'blog/about.html')


    # def detail(request, post_id):
    #     try:
    #         post = Post.objects.get(pk=post_id)
    #     except Post.DoesNotExist:
    #         raise Http404("Question does not exist")

    #     return render(request, 'post_detail.html', {'post': post})