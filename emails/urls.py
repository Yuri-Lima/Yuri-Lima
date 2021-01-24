
from django.urls import path
from . import views

#Path converters
urlpatterns = [
    path('contact/', views.send_email, name='email-contact'),
    path('thanks/', views.send_thanks, name='email-thanks'),
]