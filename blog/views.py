from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404)
from django.views.generic import (
    FormView,
    TemplateView,
    RedirectView,
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
from .form import PostFormHelper, PainelForm, HashtagForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, request
from django.forms.models import inlineformset_factory


formSet = CombinedFormSet = inlineformset_factory(
            Painel,
            Post,
            fields= ('title','content', 'url', 'contact_number', 'author', ),
            # form= PostFormHelper,
            extra=1,
            can_delete=False,
            # max_num=1,
            # validate_max= 1,
)


class PainelList(ListView):
    model: Painel
    template_name = 'painel/painel_list.html'
    paginate_by = 5 
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all
        context = {
            'posts': Post.objects.all(),
            'paineis' : Painel.objects.all()
        }
        return context

    def get_queryset(self, **kwargs):
        return Painel.objects.all().order_by('-painel_date_posted')

class PainelCreate(LoginRequiredMixin,CreateView):
    model = Painel # Painel
    form_class = PainelForm
    template_name = 'painel/painel_form.html' 

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        post_form = formSet(self.request.POST, prefix='posts') 

        if (form.is_valid() and post_form.is_valid()):
            return self.form_valid(form, post_form)

        return self.form_invalid(form, post_form)

    def form_valid(self, form, post_form):
        """
        Called if all forms are valid. Creates a Author instance along
        with associated books and then redirects to a success page.
        """
        form.instance.created_by = self.request.user
        self.object = form.save()
        post_form.instance = self.object
        post_form.save()

        #To populate author instance wich post was created
        paineis = Painel.objects.all()
        painel = paineis.get(hashtag=form.instance.hashtag)
        posts_by_hashtag = painel.post_set.all()
        for post in posts_by_hashtag:
            if post.author is None:
                post.author_id = self.request.user.id
                post.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, post_form):
        """
        Called if whether a form is invalid. Re-renders the context
        data with the data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, post_form=post_form)
        )

    def get_context_data(self, **kwargs):
        """ Add formset and formhelper to the context_data. """
        ctx = super(PainelCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            ctx['form'] = PainelForm(self.request.POST)
            ctx['post_form'] = formSet(self.request.POST,  prefix='posts')
            ctx['post_formhelper'] = PostFormHelper()
        else:
            ctx['form'] = PainelForm()
            ctx['post_form'] = formSet(prefix='posts') 
            ctx['post_formhelper'] = PostFormHelper()
        return ctx
        
    def get_success_url(self):
        return reverse('painel-detail', kwargs={'hashtag': self.object.hashtag})

class PainelDetail(LoginRequiredMixin,DetailView):
    model: Painel 
    template_name = 'painel/painel_detail.html'

    def get_object(self, queryset=None): #https://levelup.gitconnected.com/django-quick-tips-get-absolute-url-1c22321f806b
        return Painel.objects.get(hashtag=self.kwargs.get("hashtag"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        painel = Painel.objects.get(hashtag=self.kwargs.get("hashtag"))
        posts_by_hashtag = painel.post_set.all()

        # Add in a QuerySet of all the books
        context['posts_by_hashtag'] = posts_by_hashtag
        return context

class UserPainelList(ListView):
    model: Painel
    template_name = 'painel/user_painel.html'
    context_object_name = 'paineis' 
    paginate_by = 2

    def get_queryset(self):
        getUser = get_user_model()
        user = get_object_or_404(getUser, username=self.kwargs.get('username')) #Ele pega o user que vem pela URL
        return Painel.objects.filter(created_by=user)
        

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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['painel_list'] = Painel.objects.all()
        return context

class PostCreateView(LoginRequiredMixin,CreateView):
    model: Post 
    fields = ['title', 'content', 'url','contact_number']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):#"""If the form is valid, save the associated model."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        # painel = Post.objects.get(painel=self.request.painel.id)
        return Post.objects.all()

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     painelpost = Post.objects.get(painel=self.kwargs.get("hashtag"))
    #     print('Painelpost:',painelpost)
    #     # Add in a QuerySet of all the books
    #     context['post_list'] = Post.objects.all().filter(painel=painelpost)
    #     return context
    

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