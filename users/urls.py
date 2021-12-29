
#Authenticaios Users
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.forms import EmailValidationOnForgotPassword

from django.urls import path


#Path converters
urlpatterns = [
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
] 














