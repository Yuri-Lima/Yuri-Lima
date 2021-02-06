from django import forms
from django.db.models.base import Model
from .models import Painel, Post

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Painel
        fields = ('hashtag',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('painel','title','content','url','contact_number',)