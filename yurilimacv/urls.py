
from django.urls import path
from . import views

#Path converters
urlpatterns = [
    path('yurilima/', views.YuriLima, name='#yurilima'),    
    path('yurilima/about', views.YuriLimaAbout, name='#about'),
    path('yurilima/resume', views.YuriLimaResume, name='#resume'),
    path('yurilima/portfolio', views.YuriLimaPortofolio, name='#portofolio'),
    path('yurilima/services', views.YuriLimaServices, name='#services'),
    path('yurilima/contact', views.YuriLimaContact, name='#contact'), 
] 