"""yurilima URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Path converters
from django.urls import path, include, re_path
#Google Robots >> robots.txt <<
from django.views.generic import TemplateView
#Admin
from django.contrib import admin
#Static Paths >> static <<
from django.conf import settings
from django.conf.urls.static import static
#Index
from yurilimacv import views
from yurilimacv import sitemaps
#Sitemap from django
from django.contrib.sitemaps.views import sitemap
#Sitemaps from apps
from yurilimacv.sitemaps import YuriLimaCvViewSitemap
from users.sitemaps import UsersViewSitemap
from blog.sitemaps import BoardViewSitemap, PostViewSitemap
from emails.sitemaps import EmailViewSitemap

#Dict Sitemaps
# https://www.youtube.com/watch?v=xAXMqiPSY34
sitemaps = {
    'yurilimacv': YuriLimaCvViewSitemap,
    'users': UsersViewSitemap,
    'boards': BoardViewSitemap,
    'posts': PostViewSitemap,
    'email' : EmailViewSitemap,
}

#Path converters
urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    #Users and Profile
    path('', include('users.urls')),
    
    #Main Page Blog >> Posts and Painel <<
    path('blog/', include('blog.urls')),

    #Blog Emails >> anymail <<
    path('', include('emails.urls')),

    #Yuri Lima CV >> Personal <<
    path('yurilima/', include('yurilimacv.urls')),

    #Index
    path('', views.index_view),
    
    #Blog richtextfield >> ckeditor <<
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #Google Analytics >> google_analytics << https://pypi.org/project/django-google-analytics-app/
    re_path('djga/', include('google_analytics.urls')),

    #Google Robots >> robots.txt << https://developers.google.com/search/docs/advanced/robots/create-robots-txt?hl=en
    #https://stackoverflow.com/questions/58098342/how-to-make-a-robots-txt-on-django
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

    #Sitemaps >> sitemap.py <<
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]

#Static Paths >> static <<
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Error Paths Blog >> error_blog <<
handler404 = 'blog.views.error_404_view'
handler500 = 'blog.views.error_500_view'
handler403 = 'blog.views.error_403_view'
handler400 = 'blog.views.error_400_view'
