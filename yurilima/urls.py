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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from users import views as user_views
from users.forms import EmailValidationOnForgotPassword
from django.conf import settings
from django.conf.urls.static import static
from yurilimacv import views

#Path converters
urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    
    #Authenticaios Users
    path('register/', user_views.register, name='register'),#from users import views as user_views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),#from django.contrib.auth import views as auth_views
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),#from django.contrib.auth import views as auth_views  - 'users/logout.html'
    
    #Password Reset
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', form_class=EmailValidationOnForgotPassword),
         name='password_reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    #Profiles
    path('profile/', user_views.profile, name='profile'),
    
    #Main Page Blog >> Posts and Painel <<
    path('blog/', include('blog.urls')),
    # path('', include('blog.urls')),

    #Blog Emails >> anymail <<
    path('', include('emails.urls')),

    #Yuri Lima CV >> Personal <<
    path('yurilima/', include('yurilimacv.urls')),

    #Index
    path('', views.index_view),
    

    #Blog richtextfield >> tinymce <<
    path('tinymce/', include('tinymce.urls')),

    #Google Analytics >> google_analytics << https://pypi.org/project/django-google-analytics-app/
    re_path('djga/', include('google_analytics.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'blog.views.error_404_view'
handler500 = 'blog.views.error_500_view'
handler403 = 'blog.views.error_403_view'
handler400 = 'blog.views.error_400_view'
