from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import admin as auth_admin
from django.db import models
from .models import User, Profile

from .forms import UserSignup,UserUpdateForm

# Register your models here.
# admin.site.register(Profile)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form : UserUpdateForm
    add_form = UserSignup
    model = User,Profile
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        ('Aditionals Informations', {'fields': ('country','state','city')}),
    )
    # fieldsets = auth_admin.UserAdmin.fieldsets + (
    #     ('Aditionals Informations', {'fields': ('country','state','city')}),
    # )

#https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    # fields = ('user','image','bio',)