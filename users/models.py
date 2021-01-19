from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from PIL import Image
from django.contrib.auth import get_user_model


# Create your models here. https://www.geeksforgeeks.org/creating-custom-user-model-using-abstractuser-in-django_restframework/
class User(AbstractUser):
    #Perfil
    middle_name = models.CharField(max_length=150, blank=False)
    #Address
    country = models.CharField(max_length=150, blank=False)
    state = models.CharField(max_length=150, blank=False)
    city = models.CharField(max_length=150, blank=False)
    
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

class Profile(models.Model):#https://docs.djangoproject.com/pt-br/3.1/ref/models/fields/
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', unique=True)#http://fosshelp.blogspot.com/2016/11/python-django-attributeerror-user.html
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):#Django - TypeError - save() got an unexpected keyword argument 'force_insert'
        super(Profile,self).save(*args,**kwargs) #https://www.youtube.com/watch?v=A7LtgqbO9m8
        img =Image.open(self.image.path)#Just to rezise the profile image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size,reducing_gap=2.0)
            img.save(self.image.path, filename = "yuri_lima")
