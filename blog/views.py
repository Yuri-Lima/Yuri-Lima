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
from .models import Post, Painel
from users.models import Profile
from django.urls import reverse
from django.urls import reverse_lazy


class PainelList(ListView): 
    model: Painel
    template_name = 'painel/painel_list.html'
    paginate_by = 5 

    def get_queryset(self):
        return Painel.objects.all().order_by('-painel_date_posted')
    
class PainelCreate(LoginRequiredMixin,CreateView):
    model = Painel
    template_name = 'painel/painel_form.html'
    fields = ['hashtag','date_posted','date_updated']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PainelDetail(LoginRequiredMixin,DetailView):
    model: Painel 
    template_name = 'painel/painel_detail.html'

    def get_object(self, queryset=None): #https://levelup.gitconnected.com/django-quick-tips-get-absolute-url-1c22321f806b
        return Painel.objects.get(pk=self.kwargs.get("pk"))

class PainelUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Painel
    fields = ['hashtag',]
    template_name = 'painel/painel_form.html'

    def form_valid(self, form):#"""If the form is valid, save the associated model."""
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Painel.objects.all()

    def test_func(self):
        painel = self.get_object()
        if self.request.user == painel.created_by:
            return True
        return False

class PainelDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Painel
    template_name = 'painel/painel_confirm_delete.html'
    success_url = reverse_lazy('painel-list')

    def test_func(self):
        painel = self.get_object()
        if self.request.user == painel.created_by:
            return True
        return False








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