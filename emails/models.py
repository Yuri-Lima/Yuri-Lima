from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class SendContactEmail(models.Model):
    subject = models.CharField(max_length=150)
    message = models.TextField()
    from_email = models.EmailField()
    to_email = models.EmailField()

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return f"/contact/thanks/"
    
    # def get_absolute_url(self):
    #     return reverse('email-contact', kwargs={'pk': self.pk})