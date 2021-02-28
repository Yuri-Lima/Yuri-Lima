
from django.urls import path
from . import views

#Path converters
urlpatterns = [
    path('', views.YuriLima, name='#yurilima'),    
    path('about/', views.YuriLimaAbout, name='#about'),
    path('resume/', views.YuriLimaResume, name='#resume'),
    path('portfolio/', views.YuriLimaPortofolio, name='#portofolio'),
    path('services/', views.YuriLimaServices, name='#services'),
    path('contact/', views.YuriLimaContact, name='#contact'),
] 