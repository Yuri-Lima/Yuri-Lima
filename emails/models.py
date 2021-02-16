from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import User

UserModel = get_user_model()
# Create your models here.
class SendContactEmail(models.Model):
    subject = models.CharField(max_length=150)
    message = models.TextField()
    from_email = models.EmailField(verbose_name='Email', max_length=60, default=UserModel.USERNAME_FIELD)
    to_email = models.EmailField()

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return f"/contact/thanks/"