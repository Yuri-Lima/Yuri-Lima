from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Painel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    hashtag = models.CharField(max_length=255, unique=True, blank=False, null=True)
    painel_date_posted = models.DateTimeField(auto_now_add= True, null=True)
    painel_date_updated = models.DateTimeField(auto_now= True, null=True)

    def __str__(self):
        return self.hashtag

    def clean(self):
        if  self.hashtag.startswith('#'):
            self.hashtag = self.hashtag.lower()
        else:   
            self.hashtag = '#' + self.hashtag.lower()
    class Meta:
        ordering = ['-painel_date_posted']

    def get_absolute_url(self):
        return reverse('painel-detail', kwargs={'hashtag': self.hashtag})

class Post(models.Model):
    #===============================================================================
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    painel = models.ForeignKey(Painel, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100 ,null=True)
    #===============================================================================
    content_post = RichTextUploadingField(null=True, blank=True, verbose_name='Content', 
                                external_plugin_resources= [(
                                    'youtube',
                                    '/static/ckeditor/youtube/',
                                    'plugin.js',
                                )],
                                )
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
    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

