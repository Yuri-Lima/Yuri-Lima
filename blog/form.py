from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Painel, Post
#https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#django.forms.ModelForm
class PainelForm(ModelForm):
    class Meta:
        model = Painel
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
