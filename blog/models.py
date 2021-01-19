from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

class Post(models.Model):
    
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    #===============================================================================
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # authors = models.ManyToManyField(Author)
    # author_email = models.EmailField(null=True, default='')
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100 ,null=True)
    #===============================================================================
    content = models.TextField(null=True, help_text='Write your Post', blank=False)
    url = models.URLField(help_text='Paste here the link, witch you saw that news?', blank=False, default='www.exemplo.com')
    contact_number = models.CharField(max_length=20,blank=True, help_text='If you have another way to comunicate.')
    #===============================================================================
    date_posted = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateTimeField(auto_now= True)
    #===============================================================================
    # number_of_comments = models.IntegerField(null=True)
    # number_of_pingbacks = models.IntegerField(null=True)
    #===============================================================================
    # rating = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/post/{self.pk}/"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

