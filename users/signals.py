#https://docs.djangoproject.com/en/3.1/topics/signals/
# https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
from django.db.models.signals import post_save
from django.dispatch import receiver# The RECEIVER
from django.conf import settings

from .models import  Profile

# https://gist.github.com/kylefox/177091bd8e4d88ac0cc19496064fd7d3
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs): #Create profiel FUNCTION, we want to run everytime when a user has been created
    if created: #if created is False it means there any profiles has been created
        Profile.objects.create(user=instance)
        
        

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    
post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
post_save.connect(save_profile, sender=settings.AUTH_USER_MODEL)#https://docs.djangoproject.com/en/3.1/topics/auth/customizing/